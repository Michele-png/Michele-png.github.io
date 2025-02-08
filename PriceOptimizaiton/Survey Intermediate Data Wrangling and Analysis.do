*############################### Data Wrangling #############################

// Encode relevant variables
	encode gender, gen(gender_e)
	encode age, gen(age_e)
	encode region, gen(region_e)
	encode education, gen(education_e)
	encode employment, gen(employment_e)
	encode income, gen(income_e)
	encode exp_time_for_benefits, gen(exp_time_for_benefits_e)
	encode des_relieve_stress, gen (des_relieve_stress_e)
	encode des_to_impr_concent, gen (des_to_impr_concent_e)
	encode meditation_duration, gen(meditation_duration_e)
	encode meditation_frequency, gen(meditation_frequency_e)
	
//Compute Indeces 
	destring strug_enter_attion strug_keep_attion lack_of_control lack_of_efficacy, replace
	egen intermediate_self_efficacy = rmean(strug_enter_attion strug_keep_attion lack_of_control lack_of_efficacy)
	gen self_efficacy = 5 - intermediate_self_efficacy

	replace stress_1 = "1" if stress_1 == "Never"
	replace stress_1 = "2" if stress_1 == "Almost never"
	replace stress_1 = "3" if stress_1 == "Sometimes" | stress_1 == "Prefer not to say"
	replace stress_1 = "4" if stress_1 == "Fairly often"
	replace stress_1 = "5" if stress_1 == "Very often"
	replace stress_2 = "5" if stress_2 == "Never"
	replace stress_2 = "4" if stress_2 == "Almost never"
	replace stress_2 = "3" if stress_2 == "Sometimes" | stress_2 == "Prefer not to say"
	replace stress_2 = "2" if stress_2 == "Fairly often"
	replace stress_2 = "1" if stress_2 == "Very often"
	replace stress_3 = "5" if stress_3 == "Never"
	replace stress_3 = "4" if stress_3 == "Almost never"
	replace stress_3 = "3" if stress_3 == "Sometimes" | stress_3 == "Prefer not to say"
	replace stress_3 = "2" if stress_3 == "Fairly often"
	replace stress_3 = "1" if stress_3 == "Very often"
	replace stress_4 = "1" if stress_4 == "Never"
	replace stress_4 = "2" if stress_4 == "Almost never"
	replace stress_4 = "3" if stress_4 == "Sometimes" | stress_4 == "Prefer not to say"
	replace stress_4 = "4" if stress_4 == "Fairly often"
	replace stress_4 = "5" if stress_4 == "Very often"
	destring stress_1 stress_2 stress_3 stress_4, replace 
	egen intermediate_stress_level = rmean(stress_1 stress_2 stress_3 stress_4)
	gen stress_level = 5 - intermediate_stress_level

//Generate relevant cross variables
	gen hater = (meditated == "No") & (want_to_try == "Probably not" | want_to_try == "Definitely not")
	gen newbuy = (meditated == "No") & (want_to_try == "Definitely yes" | want_to_try == "Probably yes" | want_to_try ==  "Might or might not")
	gen meditators = (meditated == "Yes")
	
	split exp_benefits, parse(,)
	gen nb_exp_focusonmoment = (exp_benefits1 == "Ability to focus on the moment" | exp_benefits2 == "Ability to focus on the moment" | exp_benefits3 == "Ability to focus on the moment" | exp_benefits4 == "Ability to focus on the moment" | exp_benefits5 == "Ability to focus on the moment" | exp_benefits6 == "Ability to focus on the moment" | exp_benefits7 == "Ability to focus on the moment")
	gen nb_exp_selfcomprehension = (exp_benefits1 == "Increase your ability to comprehend your behaviours and emotions" | exp_benefits2 == "Increase your ability to comprehend your behaviours and emotions" | exp_benefits3 == "Increase your ability to comprehend your behaviours and emotions" | exp_benefits4 == "Increase your ability to comprehend your behaviours and emotions" | exp_benefits5 == "Increase your ability to comprehend your behaviours and emotions" | exp_benefits6 == "Increase your ability to comprehend your behaviours and emotions" | exp_benefits7 == "Increase your ability to comprehend your behaviours and emotions")
	gen nb_exp_concentration = (exp_benefits1 == "Increase in concentration" | exp_benefits2 == "Increase in concentration" | exp_benefits3 == "Increase in concentration" | exp_benefits4 == "Increase in concentration" | exp_benefits5 == "Increase in concentration" | exp_benefits6 == "Increase in concentration" | exp_benefits7 == "Increase in concentration")
	gen nb_exp_memory = (exp_benefits1 == "Improved memory (ability to recall and retain information)" | exp_benefits2 == "Improved memory (ability to recall and retain information)" | exp_benefits3 == "Improved memory (ability to recall and retain information)" | exp_benefits4 == "Improved memory (ability to recall and retain information)" | exp_benefits5 == "Improved memory (ability to recall and retain information)" | exp_benefits6 == "Improved memory (ability to recall and retain information)" | exp_benefits7 == "Improved memory (ability to recall and retain information)")
	gen nb_exp_productivity = (exp_benefits1 == "Improved productivity" | exp_benefits2 == "Improved productivity" | exp_benefits3 == "Improved productivity" | exp_benefits4 == "Improved productivity" | exp_benefits5 == "Improved productivity" | exp_benefits6 == "Improved productivity" | exp_benefits7 == "Improved productivity")
	gen nb_exp_jobcalmity = (exp_benefits1 == "Handling job-related stress" | exp_benefits2 == "Handling job-related stress" | exp_benefits3 == "Handling job-related stress" | exp_benefits4 == "Handling job-related stress" | exp_benefits5 == "Handling job-related stress" | exp_benefits6 == "Handling job-related stress" | exp_benefits7 == "Handling job-related stress")
	gen nb_exp_lifecalmity = (exp_benefits1 == "Handling stress due to personal life" | exp_benefits2 == "Handling stress due to personal life" | exp_benefits3 == "Handling stress due to personal life" | exp_benefits4 == "Handling stress due to personal life" | exp_benefits5 == "Handling stress due to personal life" | exp_benefits6 == "Handling stress due to personal life" | exp_benefits7 == "Handling stress due to personal life")
	egen nb_expectations = rsum(nb_exp_focusonmoment nb_exp_selfcomprehension nb_exp_concentration nb_exp_productivity nb_exp_productivity nb_exp_jobcalmity nb_exp_lifecalmity)
	
	split further_incentive, parse(,)
	gen nb_fi_friend = (further_incentive1 == "Advice of a friend" | further_incentive2 == "Advice of a friend" | further_incentive3 == "Advice of a friend" | further_incentive4 == "Advice of a friend")
	gen nb_fi_therapist = (further_incentive1 == "Advice of a therapist" | further_incentive2 == "Advice of a therapist" | further_incentive3 == "Advice of a therapist" | further_incentive4 == "Advice of a therapist")
	gen nb_fi_colleagues = (further_incentive1 == "Advice of colleagues" | further_incentive2 == "Advice of colleagues" | further_incentive3 == "Advice of colleagues" | further_incentive4 == "Advice of colleagues")
	gen nb_fi_influencer = (further_incentive1 == "Advice of an influencer" | further_incentive2 == "Advice of an influencer" | further_incentive3 == "Advice of an influencer" | further_incentive4 == "Advice of an influencer")
	gen nb_fi_professional = (further_incentive1 == "Finding a professional on which to rely on" | further_incentive2 == "Finding a professional on which to rely on" | further_incentive3 == "Finding a professional on which to rely on" | further_incentive4 == "Finding a professional on which to rely on")
	egen bn_further_incentive = rsum(nb_fi_friend nb_fi_therapist nb_fi_colleagues nb_fi_influencer nb_fi_professional)
	
	split starting_place, parse(,)
	gen nb_sp_app = (starting_place1 == "App (Calm" | starting_place2 == "App (Calm" | starting_place3 == "App (Calm" | starting_place4 == "App (Calm")
	gen nb_sp_youtube = (starting_place1 == "Youtube channels" | starting_place2 == "Youtube channels" | starting_place3 == "Youtube channels" | starting_place4 == "Youtube channels")
	gen nb_sp_centre = (starting_place1 == "Meditation Centre" | starting_place2 == "Meditation Centre" | starting_place3 == "Meditation Centre" | starting_place4 == "Meditation Centre")
	gen nb_sp_instructor = (starting_place1 == "Private instructor" | starting_place2 == "Private instructor" | starting_place3 == "Private instructor" | starting_place4 == "Private instructor")
	egen nb_start_place = rsum(nb_sp_app nb_sp_youtube nb_sp_centre nb_sp_instructor)
	
	split reason_not_want_try, parse(,)
	gen ht_rnt_time = (reason_not_want_try1 == "I have insufficient time" | reason_not_want_try2 == "I have insufficient time" | reason_not_want_try3 == "I have insufficient time")
	gen ht_rnt_benfits = (reason_not_want_try1 == "I think the benefits are insufficient" | reason_not_want_try2 == "I think the benefits are insufficient" | reason_not_want_try3 == "I think the benefits are insufficient")
	gen ht_rnt_knowledge = (reason_not_want_try1 == "I have never listened about it" | reason_not_want_try2 == "I have never listened about it" | reason_not_want_try3 == "I have never listened about it")
	gen ht_rnt_discomfort = (reason_not_want_try1 == "I think it is an uncomfortable practice" | reason_not_want_try2 == "I think it is an uncomfortable practice" | reason_not_want_try3 == "I think it is an uncomfortable practice")
	gen ht_rnt_distance = (reason_not_want_try1 == "There is no meditation centre near home" | reason_not_want_try2 == "There is no meditation centre near home" | reason_not_want_try3 == "There is no meditation centre near home")
	egen ht_reason_not_want_try = rsum(ht_rnt_time ht_rnt_benfits ht_rnt_knowledge ht_rnt_discomfort ht_rnt_distance)
	
	egen med_dur_freq = concat(meditation_duration_e meditation_frequency_e), format(%8.0f)
	encode med_dur_freq, gen(med_dur_freq_e)
	
	split usual_meditation_medium, parse(,)
	gen md_umm_app = (usual_meditation_medium1 == "App (Calm" | usual_meditation_medium2 == "App (Calm" | usual_meditation_medium3 == "App (Calm" | usual_meditation_medium4 == "App (Calm")
	gen md_umm_youtube = (usual_meditation_medium1 == "Youtube channels" | usual_meditation_medium2 == "Youtube channels" | usual_meditation_medium3 == "Youtube channels" | usual_meditation_medium4 == "Youtube channels")
	gen md_umm_centre = (usual_meditation_medium1 == "Meditation Centre" | usual_meditation_medium2 == "Meditation Centre" | usual_meditation_medium3 == "Meditation Centre" | usual_meditation_medium4 == "Meditation Centre")
	gen md_umm_instructor = (usual_meditation_medium1 == "Private instructor" | usual_meditation_medium2 == "Private instructor" | usual_meditation_medium3 == "Private instructor" | usual_meditation_medium4 == "Private instructor")
	egen md_usual_meditation_medium = rsum(md_umm_app md_umm_youtube md_umm_centre md_umm_instructor)
	
	egen competitor1 = concat(group_comp1 location_comp1 price_comp1)
	egen competitor2 = concat(group_comp2 location_comp2 price_comp2)
	encode competitor1, gen(competitor1_e)
	encode competitor2, gen(competitor2_e)

	
* ########################## Analysis ######################################
// Making lasso on a logit as if all different people responded once, each given one choice set. But controlling for the competing choice sets 
	
	// CUSTOMER PROFILE AND CONDITIONS: dioing this for newbuys 
	keep if newbuy == 1	
	lasso logit choosed competitor1_e competitor2_e individual age_e#individual gender_e#individual employment_e#individual largegroup10 age_e#largegroup10 gender_e#largegroup10 employment_e#largegroup10 smallgroup10 age_e#smallgroup10 gender_e#smallgroup10 employment_e#smallgroup10 athomewiththeinstructor age_e#athomewiththeinstructor education_e#athomewiththeinstructor region_e#athomewiththeinstructor atthemeditationcenter age_e#atthemeditationcenter education_e#atthemeditationcenter region_e#atthemeditationcenter online age_e#online education_e#online region_e#online outsideatthepark  age_e#outsideatthepark education_e#outsideatthepark region_e#outsideatthepark â1000 income_e#â1000 employment_e#â1000 â2500 region_e#â2500 income_e#â2500 employment_e#â2500 â4000 region_e#â4000 income_e#â4000 employment_e#â4000 c.self_efficacy#individual c.stress_level#individual largegroup10 c.self_efficacy#largegroup10 c.stress_level#largegroup10 smallgroup10 c.self_efficacy#smallgroup10 c.stress_level#smallgroup10 athomewiththeinstructor c.self_efficacy#athomewiththeinstructor c.stress_level#athomewiththeinstructor atthemeditationcenter c.self_efficacy#atthemeditationcenter c.stress_level#atthemeditationcenter online c.self_efficacy#online c.stress_level#online outsideatthepark c.self_efficacy#outsideatthepark c.stress_level#outsideatthepark â1000 c.self_efficacy#â1000 c.stress_level#â1000 â2500 c.self_efficacy#â2500 c.stress_level#â2500 â4000  c.self_efficacy#â4000 c.stress_level#â4000 c.nb_expectations#individual c.nb_start_place#individual exp_time_for_benefits_e#individual largegroup10 c.nb_expectations#largegroup10 c.nb_start_place#largegroup10 exp_time_for_benefits_e#largegroup10 smallgroup10 c.nb_expectations#smallgroup10 c.nb_start_place#smallgroup10 exp_time_for_benefits_e#smallgroup10 athomewiththeinstructor c.nb_expectations#athomewiththeinstructor c.nb_start_place#athomewiththeinstructor exp_time_for_benefits_e#athomewiththeinstructor atthemeditationcenter c.nb_expectations#atthemeditationcenter c.nb_start_place#atthemeditationcenter exp_time_for_benefits_e#atthemeditationcenter online c.nb_expectations#online c.nb_start_place#online exp_time_for_benefits_e#online outsideatthepark  c.nb_expectations#outsideatthepark c.nb_start_place#outsideatthepark exp_time_for_benefits_e#outsideatthepark â1000 c.nb_expectations#â4000 c.bn_further_incentive#â1000 exp_time_for_benefits_e#â1000 â2500 c.nb_expectations#â2500 c.bn_further_incentive#â2500 exp_time_for_benefits_e#â2500 â4000 c.nb_expectations#â4000 c.bn_further_incentive#â4000 exp_time_for_benefits_e#â4000, selection(adaptive)
	 
	lassocoef, display(coef, postselection format(%6.2f)) sort(coef, postselection) nolegend
	drop prob prediction_newbuy mistake_newbuy earnings
	predict prob, postselection
	gen prediction_newbuy = (prob >= 0.5)
	gen mistake_newbuy = abs(choosed - prediction_newbuy)
	summarize mistake_newbuy
	display r(mean)
	gen earnings = prediction_newbuy*(10*(â1000 == 1) + 25*(â2500 == 1) + 40*(â4000))
	display r(sum)
	
	// CUSTOMER PROFILE AND CONDITIONS doing for haters
	keep if hater == 1 
	lasso logit choosed competitor1_e competitor2_e individual age_e#individual gender_e#individual employment_e#individual largegroup10 age_e#largegroup10 gender_e#largegroup10 employment_e#largegroup10 smallgroup10 age_e#smallgroup10 gender_e#smallgroup10 employment_e#smallgroup10 athomewiththeinstructor age_e#athomewiththeinstructor education_e#athomewiththeinstructor region_e#athomewiththeinstructor atthemeditationcenter age_e#atthemeditationcenter education_e#atthemeditationcenter region_e#atthemeditationcenter online age_e#online education_e#online region_e#online outsideatthepark  age_e#outsideatthepark education_e#outsideatthepark region_e#outsideatthepark â1000 region_e#â4000 income_e#â1000 employment_e#â1000 â2500 region_e#â2500 income_e#â2500 employment_e#â2500 â4000 region_e#â4000 income_e#â4000 employment_e#â4000 c.self_efficacy#individual c.stress_level#individual largegroup10 c.self_efficacy#largegroup10 c.stress_level#largegroup10 smallgroup10 c.self_efficacy#smallgroup10 c.stress_level#smallgroup10 athomewiththeinstructor c.self_efficacy#athomewiththeinstructor c.stress_level#athomewiththeinstructor atthemeditationcenter c.self_efficacy#atthemeditationcenter c.stress_level#atthemeditationcenter online c.self_efficacy#online c.stress_level#online outsideatthepark c.self_efficacy#outsideatthepark c.stress_level#outsideatthepark â1000 c.self_efficacy#â1000 c.stress_level#â1000 â2500 c.self_efficacy#â2500 c.stress_level#â2500 â4000  c.self_efficacy#â4000 c.stress_level#â4000 c.ht_reason_not_want_try#individual des_relieve_stress_e#individual des_to_impr_concent_e#individual largegroup10 c.ht_reason_not_want_try#largegroup10 des_relieve_stress_e#largegroup10 des_to_impr_concent_e#largegroup10 smallgroup10 c.ht_reason_not_want_try#smallgroup10 des_relieve_stress_e#smallgroup10 des_to_impr_concent_e#smallgroup10 athomewiththeinstructor c.ht_reason_not_want_try#athomewiththeinstructor des_relieve_stress_e#athomewiththeinstructor des_to_impr_concent_e#athomewiththeinstructor atthemeditationcenter c.ht_reason_not_want_try#atthemeditationcenter des_relieve_stress_e#atthemeditationcenter des_to_impr_concent_e#atthemeditationcenter online c.ht_reason_not_want_try#online des_relieve_stress_e#online des_to_impr_concent_e#online outsideatthepark  c.ht_reason_not_want_try#outsideatthepark des_relieve_stress_e#outsideatthepark des_to_impr_concent_e#outsideatthepark â1000 c.ht_reason_not_want_try#â4000 des_relieve_stress_e#â1000 des_to_impr_concent_e#â1000 â2500 c.ht_reason_not_want_try#â2500 des_relieve_stress_e#â2500 des_to_impr_concent_e#â2500 â4000 c.ht_reason_not_want_try#â4000 des_relieve_stress_e#â4000 des_to_impr_concent_e#â4000, selection(adaptive)

	lassocoef, display(coef, postselection format(%6.2f)) sort(coef, postselection) nolegend
	drop prob prediction_hater mistake_hater earnings
	predict prob, postselection 
	gen prediction_hater = (prob >= 0.5)
	gen mistake_hater = abs(choosed - prediction_hater)
	summarize mistake_hater
	display r(mean)
	gen earnings = prediction_hater*(10*(â1000 == 1) + 25*(â2500 == 1) + 40*(â4000))
	display r(sum)
	
	//CUSTOMER PROFIE AND CONDITIONS: do it it for meditatators
	keep if meditators == 1 
	lasso logit choosed competitor1_e competitor2_e individual age_e#individual gender_e#individual employment_e#individual largegroup10 age_e#largegroup10 gender_e#largegroup10 employment_e#largegroup10 smallgroup10 age_e#smallgroup10 gender_e#smallgroup10 employment_e#smallgroup10 athomewiththeinstructor age_e#athomewiththeinstructor education_e#athomewiththeinstructor region_e#athomewiththeinstructor atthemeditationcenter age_e#atthemeditationcenter education_e#atthemeditationcenter region_e#atthemeditationcenter online age_e#online education_e#online region_e#online outsideatthepark  age_e#outsideatthepark education_e#outsideatthepark region_e#outsideatthepark â1000 region_e#â4000 income_e#â1000 employment_e#â1000 â2500 region_e#â2500 income_e#â2500 employment_e#â2500 â4000 region_e#â4000 income_e#â4000 employment_e#â4000 c.self_efficacy#individual c.stress_level#individual largegroup10 c.self_efficacy#largegroup10 c.stress_level#largegroup10 smallgroup10 c.self_efficacy#smallgroup10 c.stress_level#smallgroup10 athomewiththeinstructor c.self_efficacy#athomewiththeinstructor c.stress_level#athomewiththeinstructor atthemeditationcenter c.self_efficacy#atthemeditationcenter c.stress_level#atthemeditationcenter online c.self_efficacy#online c.stress_level#online outsideatthepark c.self_efficacy#outsideatthepark c.stress_level#outsideatthepark â1000 c.self_efficacy#â1000 c.stress_level#â1000 â2500 c.self_efficacy#â2500 c.stress_level#â2500 â4000  c.self_efficacy#â4000 c.stress_level#â4000 md_usual_meditation_medium#individual largegroup10 md_usual_meditation_medium#largegroup10 smallgroup10 md_usual_meditation_medium#smallgroup10 athomewiththeinstructor md_usual_meditation_medium#athomewiththeinstructor atthemeditationcenter md_usual_meditation_medium#atthemeditationcenter online md_usual_meditation_medium#online outsideatthepark md_usual_meditation_medium#outsideatthepark â1000 md_usual_meditation_medium#â1000 â2500 md_usual_meditation_medium#â2500 â4000 md_usual_meditation_medium#â4000, selection(adaptive)

	lassocoef, display(coef, postselection format(%6.2f)) sort(coef, postselection) nolegend
	drop prob prediction_meditators mistake_meditators earnings
	predict prob, postselection 
	gen prediction_meditators = (prob >= 0.5)
	gen mistake_meditators = abs(choosed - prediction_meditators)
	summarize mistake_meditators
	display r(mean)
	gen earnings = prediction_meditators*(10*(â1000 == 1) + 25*(â2500 == 1) + 40*(â4000))
	display r(sum)