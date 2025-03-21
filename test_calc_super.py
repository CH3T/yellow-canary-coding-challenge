
import unittest
import calc_super_disb_qtr as csup

class TestSuperPipeline(unittest.TestCase):
    
    def test_calculate_super(self):
        pay_codes = {'10 - Annual Lve': 'OTE', '11 - Sck/Pers': 'OTE', '13 - Public Hol': 'OTE', '14 - LWOP': 'Not OTE', '15 - A/L Cash Out': 'OTE', '1 - Normal': 'OTE', '2 - O/T 1.5': 'Not OTE', '31 - Training': 'OTE', '3 - O/T 2.0': 'Not OTE', '43 - Travel Payable': 'Not OTE', 'A010 - Lve Ldg 17.5%': 'OTE', 'A012 - Pager/On call': 'Not OTE', 'A013 - Car B/Tax': 'OTE', 'A042 - L - TRAVEL ALLOWANCE': 'Not OTE', 'A073 - NW Site Allowance': 'OTE', 'A115 -  Incentive': 'OTE', 'DMTX - AUS marginal Tax': 'Not OTE', 'P001 - Co. Super 9.5%': 'Not OTE', 'T001 - Term A - Annual Lve': 'Not OTE', 'T002 - Term A - Lve Loading': 'Not OTE', 'T003 - Term A - Long Service Lve': 'Not OTE', 'T986 - Redundancy - With Prior Support': 'Not OTE', 'T988 - Payment in lieu of notice - Redundancy': 'OTE', 'T997 - Term G - Long Service Lve Post 17/8/93': 'Not OTE', 'T998 - Term G - Lve Loading Post 17/8/93': 'Not OTE', 'T999 - Term G - Annual Lve Post 17/8/93': 'Not OTE'}
        payslips = [{'payslip_id': '1f725d94-9e6b-474b-8b31-43558ecc3589', 'employee_code': 50015418, 'code': '1 - Normal', 'amount': 3252.02}]
        # payslips = {"Emp1": {1: 10000, 2: 15000}}
        expected = {"Emp1": {1: 950.0}}
        self.assertEqual(csup.calc_super_payables(payslips,pay_codes), expected)

    # def test_calculate_variance(self):
    #     super_payable = {"Emp1": {1: 950.0, 2: 1425.0}}
    #     disbursements = {"Emp1": {1: 500.0, 2: 1000.0}}
    #     expected = {"Emp1": {1: 450.0, 2: 425.0}}
    #     self.assertEqual(csup.calculate_variance(super_payable, disbursements), expected)



if __name__ == "__main__":
    unittest.main()        