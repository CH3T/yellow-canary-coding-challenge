import pandas as pd
import os


def calc_super_payables(payslips, pay_codes):
    """calc total paid ote and super payable"""
    # print("\n payslips",payslips)
    # print("\n pay_codes",pay_codes)
    total_ote = 0
    for pay in payslips:
        if pay["code"] in pay_codes and pay_codes[pay["code"]] == "OTE":
            total_ote += pay["amount"]
    return total_ote, total_ote * 0.095

def find_disb_qtr(disbursements):
    """Find the quarter in which each disb was made."""
    quarters = {(1, 3): "Q3", (4, 6): "Q4", (7, 9): "Q1", (10, 12): "Q2"} # creating lists of keys for qts 1,3 is Q1 for eg: Jan to Mar
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
    filename = input("enter the path to xls input-file with salary, super details ↵ \n")
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
       
        total_ote, super_payable = calc_super_payables(payslips.to_dict("records"), pay_codes)
        total_disbursed = find_disb_qtr(disbursements.to_dict("records"))
        variance = calculate_variance(total_disbursed,super_payable)
       
        results.append({
            "Employee": employee,
            "Total OTE": total_ote,
            "Super Payable": super_payable,
            "Total Disbursed": total_disbursed,
            "Variance": variance
        })
   
    results_df = pd.DataFrame(results)
    print(results_df)
    results_df.to_csv("SummaryOfSuperDisb.csv", index=False)
    print("results are saved to SummaryOfSuperDisb.csv")

if __name__ == "__main__":
    main()