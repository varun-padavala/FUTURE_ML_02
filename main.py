from src.ticket_predictor import predict_ticket

text = input("Enter support ticket: ")

category, priority = predict_ticket(text)

print("\nPrediction:")
print("Category:", category)
print("Priority:", priority)