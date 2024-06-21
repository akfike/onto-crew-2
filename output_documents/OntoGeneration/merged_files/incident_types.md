(You)->[asked_about]->(Offenses), (Offenses)->[characterized_as]->(Against_the_law), (You)->[asked_if]->(Arrested_and_booked), (Arrested_and_booked)->[within_timeframe]->(Past_12_months), (Arrested_and_booked)->[for]->(Motor_vehicle_theft)

(Past_12_months)->[within_timeframe]->(Arrested_and_booked), (Arrested_and_booked)->[for]->(Larceny_or_theft), (Motor_vehicle_theft)->[excluded_from]->(Larceny_or_theft)

(You)->[subject_of]->(Arrested_and_booked), (Past_12_months)->[within_timeframe]->(Arrested_and_booked), (Arrested_and_booked)->[for]->(Burglary), (Arrested_and_booked)->[for]->(Breaking_and_entering)

(Individual)->[was_arrested_and_booked_for]->(Aggravated_Assault), (Individual)->[was_arrested_and_booked_for]->(Forcible_Rape), (Individual)->[was_arrested_and_booked_for]->(Murder), (Individual)->[was_arrested_and_booked_for]->(Homicide), (Individual)->[was_arrested_and_booked_for]->(Nonnegligent_Manslaughter)

(Individual)->[was_arrested_and_booked_for]->(Other_Assault_including_Simple_Assault_or_Battery)

(past_12_months)->[time_frame_of]->(arrested_and_booked), (you)->[subject_of]->(arrested_and_booked), (arrested_and_booked)->[for]->(robbery)

(past_12_months)->[time_frame_of]->(arrested_and_booked), (you)->[subject_of]->(arrested_and_booked), (arrested_and_booked)->[action_related_to]->(arson)

(Respondent)->[subject_of]->(Arrest_and_booking), (Arrest_and_booking)->[action_related_to]->(Driving_under_the_influence_of_alcohol_or_drugs), (Past_12_months)->[time_frame_of]->(Arrest_and_booking)

(Respondent)->[subject_of]->(Arrest_and_booking), (Arrest_and_booking)->[action_related_to]->(Driving_under_the_influence_of_alcohol_or_drugs), (Past_12_months)->[time_frame_of]->(Arrest_and_booking)

(Respondent)->[subject_of]->(Arrest_and_booking), (Arrest_and_booking)->[action_related_to]->(Possession_of_tobacco), (Past_12_months)->[time_frame_of]->(Arrest_and_booking)

(past_12_months)->[timeframe_for]->(arrested_and_booked), (you)->[subject_of]->(arrested_and_booked), (arrested_and_booked)->[reason]->(possession,_manufacture,_or_sale_of_drugs)

(BKSEXNR)->[derived_from]->(Question_1), (BKSEXNR)->[derived_from]->(Question_2), (Question_1)->[timeframe_for]->(Past_12_months), (Question_1)->[subject_of]->(Person_being_questioned), (Question_1)->[action]->(Arrested_and_booked), (Question_1)->[reason]->(Prostitution_or_commercialized_sex), (Question_2)->[timeframe_for]->(Past_12_months), (Question_2)->[subject_of]->(Person_being_questioned), (Question_2)->[action]->(Arrested_and_booked), (Question_2)->[reason]->(Sexual_offense_excluding_rape_and_prostitution)

(past_12_months)->[time_frame]->(were_arrested_and_booked),(you)->[subject]->(were_arrested_and_booked),(were_arrested_and_booked)->[action]->(for_fraud,_possessing_stolen_goods,_or_vandalism),(fraud)->[type_of]->(crime),(possessing_stolen_goods)->[type_of]->(crime),(vandalism)->[type_of]->(crime)

(BKOTH)->[indicates_responses_about]->(offenses_not_initially_acknowledged), (Respondent)->[answers]->(survey_questions), (Offense)->[specific_act_for]->(arrest_or_booking), (Code_3)->[represents]->(specific_value_within_BKOTH), (Code_5)->[represents]->(different_specific_value_within_BKOTH), (BKOTH_(Code_3))->[assigned_when]->(respondent_fails_to_acknowledge_but_later_specifies_offense), (BKOTH_(Code_5))->[used_when]->(respondent_confirms_arrest_booking_but_fails_to_specify_offense)

(John)->[works_at]->(Google), (Mary)->[employee_of]->(Amazon), (John)->[emailed]->(Mary), (John)->[about]->(Collaboration)

(you)->[have_driven]->(vehicle), (you)->[while]->(influence_of_alcohol), (influence_of_alcohol)->[during]->(past_12_months)

(you)->[have_driven]->(vehicle), (you)->[while]->(under_the_influence_of_marijuana), (under_the_influence_of_marijuana)->[during]->(past_12_months)

(you)->[have_driven]->(vehicle), (you)->[while]->(under_the_influence_of_marijuana), (under_the_influence_of_marijuana)->[during]->(past_12_months)

(you)->[have_driven]->(vehicle), (you)->[while]->(under_the_influence_of_heroin), (under_the_influence_of_heroin)->[during]->(past_12_months)

(past_12_months)->[timeframe_of]->(action), (you)->[subject_of]->(driving), (vehicle)->[object_of]->(driving), (you)->[state]->(under_the_influence_of_[LSFILL]), (under_the_influence_of_[LSFILL])->[condition_of]->(driving)

(you)->[driven_within]->(12_months), (you)->[under_influence]->(inhalant), (you)->[driven]->(vehicle)

(you)->[driven_within]->(12_months), (you)->[under_influence]->(methamphetamine), (you)->[driven]->(vehicle)

(You)->[driven]->(Vehicle), (You)->[under_influence_of]->(Alcohol), (You)->[driven_within]->(12_months)

