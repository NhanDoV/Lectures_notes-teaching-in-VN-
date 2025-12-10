function calculateTax() {
    let income = parseFloat(document.getElementById("income").value);
    let dependents = parseInt(document.getElementById("dependents").value);
    let bhxh = parseFloat(document.getElementById("bhxh").value) || 0;
    let bhyt = parseFloat(document.getElementById("bhyt").value) || 0;
    let bhtn = parseFloat(document.getElementById("bhtn").value) || 0;

    if (isNaN(income) || income <= 0) {
        document.getElementById("result").innerHTML =
            "Please enter a valid income. (Vui lòng nhập thu nhập hợp lệ)";
        return;
    }

    // Total insurance deduction
    let insuranceRate = (bhxh + bhyt + bhtn) / 100;
    let insuranceAmount = income * insuranceRate;

    // Deductions
    let personalDeduction = 11000000;
    let dependentDeduction = dependents * 4400000;

    let taxableIncome = income - insuranceAmount - personalDeduction - dependentDeduction;

    if (taxableIncome <= 0) {
        document.getElementById("result").innerHTML =
            "No tax required. (Không phải nộp thuế)";
        return;
    }

    let tax = calculateProgressiveTax(taxableIncome);

    document.getElementById("result").innerHTML = `
        <div>Tax Payable (Thuế phải nộp): <b>${tax.toLocaleString()} VND</b></div>
        <div>Insurance Deduction (Tiền bảo hiểm): <b>${insuranceAmount.toLocaleString()} VND</b></div>
        <div>Taxable Income (Thu nhập tính thuế): <b>${taxableIncome.toLocaleString()} VND</b></div>
    `;
}

function calculateProgressiveTax(income) {
    let tax = 0;
    let brackets = [
        { limit: 5000000, rate: 0.05 },
        { limit: 10000000, rate: 0.10 },
        { limit: 18000000, rate: 0.15 },
        { limit: 32000000, rate: 0.20 },
        { limit: 52000000, rate: 0.25 },
        { limit: 80000000, rate: 0.30 },
        { limit: Infinity, rate: 0.35 }
    ];

    let previous = 0;

    for (let i = 0; i < brackets.length; i++) {
        if (income > previous) {
            let taxable = Math.min(income, brackets[i].limit) - previous;
            tax += taxable * brackets[i].rate;
            previous = brackets[i].limit;
        }
    }

    return Math.round(tax);
}