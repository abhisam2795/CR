def parseCardDetails(json_data):
	cardDetails = {}
	cardDetails["cardsWhichAreDonatable"]= json_data["cardsWhichAreDonatable"]
	cardDetails["cardsHaving"]= json_data["cardsHaving"]
	cardDetails["cardsNotUnlocked"]= json_data["cardsNotUnlocked"]
	
	return cardDetails
