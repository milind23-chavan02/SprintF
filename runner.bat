cd C:\Users\Administrator\Desktop\workspace\SPRINT2
behave -f allure_behave.formatter:AllureFormatter -o ./allure_reports features/flipkart.feature
behave --junit --junit-directory my_reports features/flipkart.feature
behave -f json.pretty -o myReports.json features/flipkart.feature