from TestFramework import TestCaseTest, TestResult, TestSuite, TestSuiteTest, TestLoader, TestLoaderTest, TestRunner

loader = TestLoader()
suite = loader.make_suite(TestLoaderTest)

runner = TestRunner()
runner.run(suite)