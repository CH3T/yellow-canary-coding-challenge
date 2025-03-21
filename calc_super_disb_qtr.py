import pandas as pd
import os


def calculate_super_payable(payslips, pay_codes):
    """Calculate total OTE and super payable."""
    print("\n payslips",payslips)
    print("\n pay_codes",pay_codes)
    total_ote = 0
    for pay in payslips:
        if pay["pay_code"] in pay_codes and pay_codes[pay["pay_code"]] == "OTE":
            total_ote += pay["Amount"]
    return total_ote, total_ote * 0.095

def determine_disbursement_quarter(disbursements):
    """Determine the quarter in which each disbursement was made."""
    quarters = {(1, 3): "Q1", (4, 6): "Q2", (7, 9): "Q3", (10, 12): "Q4"}
    disbursed_total = 0
    for disb in disbursements:
        month = pd.to_datetime(disb["payment_made"]).month
        for (start, end), q in quarters.items():
            if start <= month <= end:
                disbursed_total += disb["sgc_amount"]
                break
    return disbursed_total

def calculate_variance(super_payable, total_disbursed):
    """Calculate variance between payable and disbursed."""
    return super_payable - total_disbursed

def main():
    filename = input("enter the xls input file path with salary, super details...\n")
    if not os.path.exists(filename):
        print("file not found")
        return
   
    data = pd.read_excel(filename, sheet_name=None)
    pay_codes = {row["pay_code"]: row["ote_treament"] for _, row in data["PayCodes"].iterrows()}
    employees = data["Payslips"]["employee_code"].unique()
   
    results = []
    for employee in employees:
        payslips = data["Payslips"][data["Payslips"]["employee_code"] == employee]
        disbursements = data["Disbursements"][data["Disbursements"]["employee_code"] == employee]
       
        total_ote, super_payable = calculate_super_payable(payslips.to_dict("records"), pay_codes)
        total_disbursed = determine_disbursement_quarter(disbursements.to_dict("records"))
        variance = calculate_variance(super_payable, total_disbursed)
       
        results.append({
            "Employee": employee,
            "Total OTE": total_ote,
            "Super Payable": super_payable,
            "Total Disbursed": total_disbursed,
            "Variance": variance
        })
   
    results_df = pd.DataFrame(results)
    print(results_df)
    results_df.to_csv("super_summary.csv", index=False)
    print("Results saved to super_summary.csv")

if __name__ == "__main__":
    main()