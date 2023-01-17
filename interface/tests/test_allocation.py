from django.test import TestCase
from interface.gale_shapely import *
from unittest.mock import ANY

class GaleAllocationTest(TestCase):
    def test_gale_allocation(self):
        intern_preference = {
            'intern1': ['job1', 'job2', 'job3'],
            'intern2': ['job2', 'job1', 'job3'],
            'intern3': ['job3', 'job2', 'job1'],
        }
        job_preference = {
            'job1': ['intern1', 'intern2', 'intern3'],
            'job2': ['intern2', 'intern1', 'intern3'],
            'job3': ['intern3', 'intern1', 'intern2'],
        }
        expected_result = [('intern2', 'job2'), ('intern1', 'job1'), ('intern3', 'job3')]
        result = gale_allocation(intern_preference=intern_preference, job_preference=job_preference)
        self.assertEqual(sorted(result, key=lambda x: x[0]), sorted(expected_result, key=lambda x: x[0]))

    def test_gale_allocation_different_pref(self):
        intern_preference = {
            'intern1': ['job3', 'job2', 'job1'],
            'intern2': ['job3', 'job1', 'job2'],
            'intern3': ['job3', 'job2', 'job1'],
        }
        job_preference = {
            'job1': ['intern1', 'intern2', 'intern3'],
            'job2': ['intern3', 'intern1', 'intern2'],
            'job3': ['intern3', 'intern2', 'intern1'],
        }
        expected_result = [('intern3', 'job3'), ('intern2', 'job1'), ('intern1', 'job2')]
        result = gale_allocation(intern_preference=intern_preference, job_preference=job_preference)
        self.assertEqual(sorted(result, key=lambda x: x[0]), sorted(expected_result, key=lambda x: x[0]))


    def test_gale_allocation_empty_preference(self):
        # Test scenario 2 - Empty intern_preference
        intern_preference = {}
        job_preference = {
            'job1': ['intern1', 'intern2', 'intern3'],
            'job2': ['intern2', 'intern1', 'intern3'],
            'job3': ['intern3', 'intern1', 'intern2'],
        }
        expected_result = []
        result = gale_allocation(intern_preference=intern_preference, job_preference=job_preference)
        
        self.assertEqual(sorted(result, key=lambda x: x[0]), sorted(expected_result, key=lambda x: x[0]))

    def test_gale_allocation_same_intern_preference(self):
        intern_preference = {
            'intern1': ['job1', 'job2', 'job3'],
            'intern2': ['job1', 'job2', 'job3'],
            'intern3': ['job1', 'job2', 'job3'],
        }
        job_preference = {
            'job1': ['intern3', 'intern1', 'intern2'],
            'job2': ['intern1', 'intern3', 'intern2'],
            'job3': ['intern2', 'intern1', 'intern3'],
        }
        expected_result = [('intern1', 'job2'), ('intern2', 'job3'), ('intern3', 'job1')]
        result = gale_allocation(intern_preference=intern_preference, job_preference=job_preference)
  
        self.assertEqual(sorted(result, key=lambda x: x[0]), sorted(expected_result, key=lambda x: x[0]))
    

class ParetoOptimalTest(TestCase):
    def test_pareto_optimal(self):
        intern_preferences = {
            'intern1': ['job1', 'job2', 'job3'],
            'intern2': ['job2', 'job1', 'job3'],
            'intern3': ['job3', 'job2', 'job1'],
        }
        job_preferences = {
            'job1': ['intern1', 'intern2', 'intern3'],
            'job2': ['intern2', 'intern1', 'intern3'],
            'job3': ['intern3', 'intern1', 'intern2'],
        }
        expected_result = [('intern1', 'job1'), ('intern2', 'job2'), ('intern3', 'job3')]
        result = pareto_optimal(intern_preferences, job_preferences)

        self.assertEqual(sorted(result, key=lambda x: x[0]), sorted(expected_result, key=lambda x: x[0]))

    def test_pareto_optimal_intern_not_in_preference(self):
        # Test scenario 2 - Intern not in job_preferences
        intern_preferences = {
            'intern1': ['job1', 'job2'],
            'intern2': ['job2', 'job1'],
            'intern3': ['job3', 'job2'],
        }
        job_preferences = {
            'job1': ['intern1', 'intern2'],
            'job2': ['intern2', 'intern1'],
            'job3': ['intern3', 'intern1'],
        }
        expected_result = [('intern1', 'job1'), ('intern2', 'job2'), ('intern3', 'job3')]
        result = pareto_optimal(intern_preferences, job_preferences)

        self.assertEqual(sorted(result, key=lambda x: x[0]), sorted(expected_result, key=lambda x: x[0]))

    def test_pareto_optimal_job_not_in_preference(self):
        # Test scenario 3 - Job not in intern_preferences
        intern_preferences = {
            'intern1': ['job1', 'job2', 'job3'],
            'intern2': ['job2', 'job1', 'job3'],
            'intern3': ['job3', 'job2', 'job1'],
        }
        job_preferences = {
            'job1': ['intern1', 'intern2'],
            'job2': ['intern2', 'intern1'],
            'job3': ['intern3', 'intern1'],
        }
        expected_result = [('intern1', 'job1'), ('intern2', 'job2'), ('intern3', 'job3')]
        result = pareto_optimal(intern_preferences, job_preferences)
        self.assertCountEqual(result, expected_result)

    def test_pareto_optimal_same_intern_preference(self):
        intern_preferences = {
            'intern1': ['job1', 'job2', 'job3'],
            'intern2': ['job1', 'job2', 'job3'],
            'intern3': ['job1', 'job2', 'job3'],
        }
        job_preferences = {
            'job1': ['intern3', 'intern1', 'intern2'],
            'job2': ['intern1', 'intern3', 'intern2'],
            'job3': ['intern2', 'intern1', 'intern3'],
        }
        expected_result = [('intern1', 'job1'), ('intern2', 'job2'), ('intern3', 'job3')]
        result = pareto_optimal(intern_preferences, job_preferences)
        self.assertEqual(sorted(result, key=lambda x: x[0]), sorted(expected_result, key=lambda x: x[0]))


class HungarianAlgorithmTest(TestCase):
    def test_hungarian_algorithm(self):
        preference = {
            'intern1': ['job1', 'job2', 'job3'],
            'intern2': ['job2', 'job1', 'job3'],
            'intern3': ['job3', 'job2', 'job1'],

        }
        expected_result = [('intern1', 'job1'), ('intern3', 'job3'), ('intern2', 'job2')]
        result = hungarian_algorithm(preference)
        self.assertCountEqual(result, expected_result)

    def test_hungarian_algorithm_with_diffrent_preferences(self):
        preference = {
            'intern1': ['job1', 'job2', 'job3'],
            'intern2': ['job1', 'job2', 'job3'],
            'intern3': ['job3', 'job2', 'job1'],
        }
        expected_result = [('intern2', 'job1'), ('intern1', 'job2'), ('intern3', 'job3')]
        result = hungarian_algorithm(preference)
        self.assertCountEqual(result, expected_result)


    def test_hungarian_algorithm_with_diffrent_2_preferences(self):
        preference = {
            'intern1': ['job1', 'job2', 'job3'],
            'intern2': ['job1', 'job2', 'job3'],
            'intern3': ['job3', 'job2', 'job1'],
        }
        expected_result = [('intern2', 'job1'), ('intern1', 'job2'), ('intern3', 'job3')]
        result = hungarian_algorithm(preference)
        self.assertCountEqual(result, expected_result)