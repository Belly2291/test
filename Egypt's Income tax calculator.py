# Change monthly salary to field name to be linked with in contract if needed.
range1 = 15000
range2 = 30000
range3 = 45000
range4 = 60000
range5 = 200000
range6 = 400000
range7 = 600000
range8 = 700000
range9 = 800000
range10 = 900000
range11 = 1000000

fixedExemptedAmount = 9000
monthlySalary = contract.wage
yearlySalary = (monthlySalary * 12) - fixedExemptedAmount
taxPayableAmount = 0
fixedPaybleTaxAmount = 0

if yearlySalary <= range1:
    taxPayableAmount = 0
    result = -taxPayableAmount
elif range1 < yearlySalary <= range2:
    taxPayableAmount = ((yearlySalary - range1) * 0.025) / 12
    result = -taxPayableAmount
elif range2 < yearlySalary <= range3:
    taxPayableAmount = ((yearlySalary - range2) * 0.1 + 375) / 12
    result = -taxPayableAmount
elif range3 < yearlySalary <= range4:
    taxPayableAmount = ((yearlySalary - range3) * 0.15 + 375 + 1500) / 12
    result = -taxPayableAmount
elif range4 < yearlySalary <= range5:
    taxPayableAmount = ((yearlySalary - range4) * 0.2 + 375 + 1500 + 2250) / 12
    result = -taxPayableAmount
elif range5 < yearlySalary <= range6:
    taxPayableAmount = ((yearlySalary - range5) * 0.225 + 375 + 1500 + 2250 + 28000) / 12
    result = -taxPayableAmount
elif range6 < yearlySalary <= range7:
    taxPayableAmount = ((yearlySalary - range6) * 0.25 + 375 + 1500 + 2250 + 28000 + 45000) / 12
    result = -taxPayableAmount
elif range7 < yearlySalary <= range8:
    fixedPaybleTaxAmount = 375
    taxPayableAmount = ((yearlySalary - range6) * 0.25 + 375 + 1500 + 2250 + 28000 + 45000 + fixedPaybleTaxAmount) / 12
    result = -taxPayableAmount
elif range8 < yearlySalary <= range9:
    fixedPaybleTaxAmount = 2625
    taxPayableAmount = ((yearlySalary - range6) * 0.25 + 375 + 1500 + 2250 + 28000 + 45000 + fixedPaybleTaxAmount) / 12
    result = -taxPayableAmount
elif range9 < yearlySalary <= range10:
    fixedPaybleTaxAmount = 4875
    taxPayableAmount = ((yearlySalary - range6) * 0.25 + 375 + 1500 + 2250 + 28000 + 45000 + fixedPaybleTaxAmount) / 12
    result = -taxPayableAmount
elif range10 < yearlySalary <= range11:
    fixedPaybleTaxAmount = 7875
    taxPayableAmount = ((yearlySalary - range6) * 0.25 + 375 + 1500 + 2250 + 28000 + 45000 + fixedPaybleTaxAmount) / 12
    result = -taxPayableAmount
else:
    fixedPaybleTaxAmount = 12875
    taxPayableAmount = ((yearlySalary - range6) * 0.25 + 375 + 1500 + 2250 + 28000 + 45000 + fixedPaybleTaxAmount) / 12
    result = -taxPayableAmount
