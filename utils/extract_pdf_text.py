import os
import json
import zipfile
import logging
from datetime import datetime
from adobe.pdfservices.operation.auth.service_principal_credentials import ServicePrincipalCredentials
from adobe.pdfservices.operation.exception.exceptions import ServiceApiException, ServiceUsageException, SdkException
from adobe.pdfservices.operation.pdf_services import PDFServices
from adobe.pdfservices.operation.pdf_services_media_type import PDFServicesMediaType
from adobe.pdfservices.operation.pdfjobs.jobs.extract_pdf_job import ExtractPDFJob
from adobe.pdfservices.operation.pdfjobs.params.extract_pdf.extract_element_type import ExtractElementType
from adobe.pdfservices.operation.pdfjobs.params.extract_pdf.extract_pdf_params import ExtractPDFParams
from adobe.pdfservices.operation.pdfjobs.result.extract_pdf_result import ExtractPDFResult
import tiktoken

# Initialize the logger
logging.basicConfig(level=logging.INFO)

class ExtractTextInfoFromPDF:
    def __init__(self, pdf_path):
        try:
            with open(pdf_path, 'rb') as file:
                input_stream = file.read()

            # Initial setup, create credentials instance
            credentials = ServicePrincipalCredentials(
                client_id=os.getenv('PDF_SERVICES_CLIENT_ID'),
                client_secret=os.getenv('PDF_SERVICES_CLIENT_SECRET')
            )

            # Creates a PDF Services instance
            pdf_services = PDFServices(credentials=credentials)

            # Creates an asset from the source file
            input_asset = pdf_services.upload(input_stream=input_stream, mime_type=PDFServicesMediaType.PDF)

            # Create parameters for the job
            extract_pdf_params = ExtractPDFParams(
                elements_to_extract=[ExtractElementType.TEXT]
            )

            # Creates a new job instance
            extract_pdf_job = ExtractPDFJob(input_asset=input_asset, extract_pdf_params=extract_pdf_params)

            # Submit the job and get the job result
            location = pdf_services.submit(extract_pdf_job)
            pdf_services_response = pdf_services.get_job_result(location, ExtractPDFResult)

            # Get content from the resulting asset
            result_asset = pdf_services_response.get_result().get_resource()
            stream_asset = pdf_services.get_content(result_asset)

            # Save the result to a ZIP file
            output_zip_path = self.create_output_file_path()
            with open(output_zip_path, "wb") as file:
                file.write(stream_asset.get_input_stream())

            # Extract and parse the JSON result
            with zipfile.ZipFile(output_zip_path, 'r') as archive:
                json_entry = archive.open('structuredData.json')
                json_data = json_entry.read()
                data = json.loads(json_data)

            # Process the extracted data
            self.process_extracted_text(data, max_token_length=2048)

        except (ServiceApiException, ServiceUsageException, SdkException) as e:
            logging.exception(f'Exception encountered while executing operation: {e}')

    @staticmethod
    def create_output_file_path() -> str:
        now = datetime.now()
        time_stamp = now.strftime("%Y-%m-%dT%H-%M-%S")
        os.makedirs("output_documents/ExtractTextInfoFromPDF", exist_ok=True)
        return f"output_documents/ExtractTextInfoFromPDF/extract{time_stamp}.zip"

    def process_extracted_text(self, data, max_token_length):
        text = ''.join(item['Text'] for item in data['elements'] if 'Text' in item)
        tokens, encoder = self.tokenize_text(text)
        chunk_number = 0
        for chunk in self.chunk_tokens(tokens, max_token_length):
            self.save_chunk_to_file(chunk, encoder, chunk_number)
            chunk_number += 1

    @staticmethod
    def tokenize_text(text):
        enc = tiktoken.encoding_for_model("gpt-4")
        tokens = enc.encode(text)
        return tokens, enc

    @staticmethod
    def chunk_tokens(tokens, max_token_length):
        for i in range(0, len(tokens), max_token_length):
            yield tokens[i:i + max_token_length]

    @staticmethod
    def save_chunk_to_file(chunk, encoder, chunk_number):
        text = encoder.decode(chunk)
        filename = f'output_documents/ExtractTextInfoFromPDF/chunk_{chunk_number}.txt'
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)


if __name__ == "__main__":
    # Replace with your actual PDF path
    PDF_FILE_PATH = 'input_documents/NSF--OKN.pdf'
    ExtractTextInfoFromPDF(PDF_FILE_PATH)
