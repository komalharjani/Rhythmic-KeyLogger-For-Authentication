import excel "K:\rhythm data.xlsx", sheet("Sheet1") firstrow case(lower) clear

//generate variables that hold all inter-key times for each user
gen user1 = user1simple + user1complex
gen user2 = user2simple + user2complex
gen user3 = user3simple + user3complex

//TTEST --> Hypothesis 1
ttest user1simple == user1complex
outreg2 using OutReg, replace excel dec(3)
ttest user2simple == user2complex
outreg2 using OutReg, replace excel dec(3)
ttest user3simple == user3complex
outreg2 using OutReg, replace excel dec(3)

//regression analysis --> Hypothesis 2

reg length user1rhythm user2rhythm user3rhythm
outreg2 using OutReg1, append excel dec(3)
