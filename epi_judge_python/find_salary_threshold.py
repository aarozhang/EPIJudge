from typing import List

from test_framework import generic_test


def find_salary_cap(target_payroll: int, current_salaries: List[int]) -> float:
    current_salaries.sort()
    unadjusted_salary_sum = 0.0

    for i, current_salary in enumerate(current_salaries):
        adjusted_people = len(current_salaries) - i
        adjusted_salary_sum = current_salary * adjusted_people

        if unadjusted_salary_sum + adjusted_salary_sum >= target_payroll:
            return (target_payroll - unadjusted_salary_sum) / adjusted_people

        unadjusted_salary_sum += current_salary

    return -1.0


if __name__ == '__main__':
    print(find_salary_cap(210, [20,30,40,90,100]))
    # exit(
    #     generic_test.generic_test_main('find_salary_threshold.py',
    #                                    'find_salary_threshold.tsv',
    #                                    find_salary_cap))
