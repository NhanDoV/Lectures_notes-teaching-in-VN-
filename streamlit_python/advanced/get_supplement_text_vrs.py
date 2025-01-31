import json

def get_json_card_info(card_type):
    
    if card_type == "Thẻ thanh toán toàn cầu VIB Ivy Card":
        json_dict = {
            "card_name": "VIB Ivy Card",
            "product_type": "payment",
            "highlight-features": {
                "annual_fee": "Free maintenance in the first year",
                "reward_rate": "Super free offers",
                "interest": "No-term interest on the payment account for each period",
                "transactions_per_day": 50
            },
            "benefit": {
                "is_cashback": None,
                "is_low_interest": None,
                "for_shopping": True,
                "for_food": True,
                "for_entertainment": True,
                "for_insurance": True,
                "for_education": True
            },                
            "fees": {
                "Card Issuance and Maintenance Fees": {
                    "Card Issuance Fee": {
                        "Standard": "Free",
                        "With Custom Design": 110000,
                        "Reissue within 3 months": 110000
                    },
                    "Card Maintenance Fee per month": 10000
                },
                "ATM Transaction Fees": {
                    "Balance Inquiry / Statement within Network": "Free",
                    "Balance Inquiry / Statement outside Network": 5500,
                    "Cash Withdrawal (Domestic, outside Network)": 10000,
                    "Cash Withdrawal (International)": "4% of withdrawal amount (Minimum 50,000 VND)",
                    "Foreign Currency Transaction Fee": "4% of transaction amount (Min 10,000 VND/transaction)",
                    "Vietnamese Currency Transaction Abroad": "1.1% (Minimum 10,000 VND)"
                },
                "Other Service Fees": {
                    "Card Replacement Fee per transaction": 100000,
                    "Card Renewal Fee": "Free",
                    "Lost or Stolen Card Notification Fee per transaction": 200000,
                    "PIN Reissue Fee per transaction": 50000,
                    "Card Number Selection Fee per transaction": 200000,
                    "Product Change Fee per transaction": 100000,
                    "Dispute Fee (Incorrect Transaction) per transaction": 200000,
                    "Lost/Stolen Card Replacement Fee per transaction": 200000,
                    "Visa Direct International Money Transfer Fee per transaction": 50000,
                    "Special Service Fee per transaction": 500000
                }
            }
        }
    elif card_type == "Thẻ thanh toán VIB Online Plus 2in1":
        json_dict = {
            "card_name": "VIB Online Plus 2in1",
            "product_type": "payment",
            "highlight-features": {
                "annual_fee": "Free in the first year",
                "reward_rate": "Not specified",
                "interest": "No-term interest on the payment account for each period",
                "transactions_per_day": "Not specified"
            },
            "benefit": {
                "is_cashback": None,
                "is_low_interest": None,
                "for_shopping": True,
                "for_food": True,
                "for_entertainment": True,
                "for_insurance": True,
                "for_education": True
            },
            "mobile_payment_solutions": ["Google Pay", "Apple Pay", "Garmin Pay"],
            "fees": {
                "Card Issuance and Maintenance Fees": {
                    "Card Issuance Fee": {
                        "Standard": "Free",
                        "With Custom Design": 110000,
                        "Reissue within 3 months": 110000
                    },
                    "Card Maintenance Fee per month": 20000
                },
                "ATM Transaction Fees": {
                    "Balance Inquiry / Statement within Network": "Free",
                    "Balance Inquiry / Statement outside Network": 5500,
                    "Cash Withdrawal (Domestic, outside Network)": 10000,
                    "Cash Withdrawal (International)": "4% of withdrawal amount (Minimum 50,000 VND)",
                    "Foreign Currency Transaction Fee": "3% of transaction amount (Min 10,000 VND/transaction)",
                    "Vietnamese Currency Transaction Abroad": "1.1% (Minimum 10,000 VND)"
                },
                "Other Service Fees": {
                    "Card Replacement Fee per transaction": "Free",
                    "Card Renewal Fee": "Free",
                    "Lost or Stolen Card Notification Fee per transaction": 200000,
                    "PIN Reissue Fee per transaction": 50000,
                    "Card Number Selection Fee per transaction": 200000,
                    "Product Change Fee per transaction": 100000,
                    "Dispute Fee (Incorrect Transaction) per transaction": 200000,
                    "Express Card Issuance/Replacement Fee per transaction": 200000,
                    "Mastercard MoneySend Fee per transaction": 50000,
                    "Special Service Fee per transaction": 500000,
                    "Chargeback Service Fee": "35% of the refunded amount (if applicable)"
                }
            }
        }            
    elif card_type == "Thẻ thanh toán toàn cầu VIB Platinum":
        json_dict = {
            "card_name": "VIB Platinum",
            "product_type": "payment",
            "highlight-features": {
                "annual_fee": "Free in the first year",
                "reward_rate": "2% cashback on online transactions, 1% cashback on all other transactions",
                "interest": "No-term interest on the payment account for each period",
                "transactions_per_day": "Not specified"
            },
            "benefit": {
                "is_cashback": True,
                "is_low_interest": None,
                "for_shopping": True,
                "for_food": True,
                "for_entertainment": True,
                "for_insurance": True,
                "for_education": True
            },
            "cashback_limit_per_month": 400000,
            "mobile_payment_solutions": ["Google Pay", "Apple Pay", "Garmin Pay"],
            "fees": {
                "Card Issuance and Maintenance Fees": {
                    "Card Issuance Fee": {
                        "Standard": "Free",
                        "Reissue within 3 months": 110000
                    },
                    "Card Maintenance Fee per month": 20000
                },
                "ATM Transaction Fees": {
                    "Balance Inquiry / Statement within Network": "Free",
                    "Balance Inquiry / Statement outside Network": 5500,
                    "Cash Withdrawal (Within Network)": "Free",
                    "Cash Withdrawal (Domestic, outside Network)": 10000,
                    "Cash Withdrawal (International)": "4% of withdrawal amount (Minimum 50,000 VND)",
                    "Foreign Currency Transaction Fee": "3% of transaction amount (Min 10,000 VND/transaction)",
                    "Vietnamese Currency Transaction Abroad": "1.1% (Minimum 10,000 VND)"
                },
                "Other Service Fees": {
                    "Card Replacement Fee per transaction": 100000,
                    "Card Renewal Fee": "Free",
                    "Lost or Stolen Card Notification Fee per transaction": 200000,
                    "PIN Reissue Fee per transaction": 50000,
                    "Card Number Selection Fee per transaction": 200000,
                    "Product Change Fee per transaction": 100000,
                    "Dispute Fee (Incorrect Transaction) per transaction": 200000,
                    "Express Card Issuance/Replacement Fee per transaction": 200000,
                    "Mastercard MoneySend Fee per transaction": 50000,
                    "Card Delivery Fee (if issued at the branch)": 20000,
                    "Special Service Fee per transaction": 500000
                }
            }
        }
    elif card_type == "Thẻ thanh toán toàn cầu VIB iCard":
        json_dict = {
            "card_name": "VIB iCard",
            "product_type": "payment",
            "highlight-features": {
                "annual_fee": "Free in the first year",
                "reward_rate": "Not specified",
                "interest": "No-term interest on the payment account for each period",
                "transactions_per_day": "Not specified"
            },
            "benefit": {
                "is_cashback": None,
                "is_low_interest": None,
                "for_shopping": True,
                "for_food": True,
                "for_entertainment": True,
                "for_insurance": True,
                "for_education": True
            },
            "cashback_limit_per_month": None,
            "mobile_payment_solutions": ["Google Pay", "Apple Pay", "Garmin Pay"],
            "fees": {
                "Card Issuance and Maintenance Fees": {
                    "Card Issuance Fee": {
                        "Standard": "Free",
                        "Reissue within 3 months": 110000
                    },
                    "Card Maintenance Fee per month": 10000
                },
                "ATM Transaction Fees": {
                    "Balance Inquiry / Statement within Network": "Free",
                    "Balance Inquiry / Statement outside Network": 5500,
                    "Cash Withdrawal (Within Network)": "Free",
                    "Cash Withdrawal (Domestic, outside Network)": 10000,
                    "Cash Withdrawal (International)": "4% of withdrawal amount (Minimum 50,000 VND)",
                    "Foreign Currency Transaction Fee": "4% of transaction amount (Min 10,000 VND/transaction)",
                    "Vietnamese Currency Transaction Abroad": "1.1% (Minimum 10,000 VND)"
                },
                "Other Service Fees": {
                    "Card Replacement Fee per transaction": 100000,
                    "Card Renewal Fee": "Free",
                    "Lost or Stolen Card Notification Fee per transaction": 200000,
                    "PIN Reissue Fee per transaction": 50000,
                    "Card Number Selection Fee per transaction": 200000,
                    "Product Change Fee per transaction": 100000,
                    "Dispute Fee (Incorrect Transaction) per transaction": 200000,
                    "Express Card Issuance/Replacement Fee per transaction": 200000,
                    "Mastercard MoneySend Fee per transaction": 50000,
                    "Card Delivery Fee (if issued at the branch)": 20000,
                    "Early Card Closure Fee (within 13 months of issue)": 100000,
                    "Special Service Fee per transaction": 500000,
                    "Chargeback Service Fee": "35% of the refunded amount (if applicable)"
                }
            }
        }
    elif card_type == "Thẻ thanh toán VIB LazCard":
        json_dict = {
            "card_name": "VIB Standard Card",
            "product_type": "payment",
            "highlight-features": {
                "annual_fee": "Free in the first year",
                "reward_rate": "Not specified",
                "interest": "No-term interest on the payment account for each period",
                "transactions_per_day": "Not specified"
            },
            "benefit": {
                "is_cashback": None,
                "is_low_interest": None,
                "for_shopping": True,
                "for_food": True,
                "for_entertainment": True,
                "for_insurance": True,
                "for_education": True
            },
            "cashback_limit_per_month": None,
            "mobile_payment_solutions": ["Internet Banking", "MyVIB", "ATMs nationwide"],
            "fees": {
                "Card Issuance and Maintenance Fees": {
                    "Card Issuance Fee": {
                        "Standard": "Free",
                        "Reissue within 3 months": 110000
                    },
                    "Card Maintenance Fee per month": 20000
                },
                "ATM Transaction Fees": {
                    "Balance Inquiry / Statement within Network": "Free",
                    "Balance Inquiry / Statement outside Network": 5500,
                    "Cash Withdrawal (Domestic, outside Network)": 10000,
                    "Cash Withdrawal (International)": "4% of withdrawal amount (Minimum 50,000 VND)",
                    "Foreign Currency Transaction Fee": "3% of transaction amount (Min 10,000 VND/transaction)",
                    "Vietnamese Currency Transaction Abroad": "1.1% (Minimum 10,000 VND)"
                },
                "Other Service Fees": {
                    "Card Replacement Fee per transaction": 100000,
                    "Card Renewal Fee": "Free",
                    "Lost or Stolen Card Notification Fee per transaction": 200000,
                    "PIN Reissue Fee per transaction": 50000,
                    "Card Number Selection Fee per transaction": 200000,
                    "Dispute Fee (Incorrect Transaction) per transaction": 200000,
                    "Express Card Issuance/Replacement Fee per transaction": "Free",
                    "Visa Direct International Money Transfer Fee per transaction": 50000,
                    "Special Service Fee per transaction": 500000
                }
            }
        }
    elif card_type == "Thẻ thanh toán nội địa VIB Values (ATM)":
        json_dict = {
            "card_name": "VIB Values (ATM)",
            "product_type": "payment",
            "highlight-features": {
                "annual_fee": "66,000 VND/year",
                "reward_rate": "Up to 50% discount at VIB partners for shopping, travel, restaurants, hotels, spas, entertainment, etc.",
                "interest": "No-term interest on the payment account for each period",
                "transactions_per_day": "Not specified"
            },
            "benefit": {
                "is_cashback": None,
                "is_low_interest": None,
                "for_shopping": True,
                "for_food": True,
                "for_entertainment": True,
                "for_insurance": False,
                "for_education": False
            },
            "cashback_limit_per_month": None,
            "mobile_payment_solutions": ["Internet Banking", "MyVIB", "ATMs nationwide"],
            "fees": {
                "Card Issuance and Maintenance Fees": {
                    "Card Issuance Fee": {
                        "Main Card": "110,000 VND",
                        "Supplementary Card": "110,000 VND"
                    },
                    "Card Maintenance Fee per year": "66,000 VND"
                },
                "ATM Transaction Fees": {
                    "Balance Inquiry / Statement within Network": "Free",
                    "Balance Inquiry / Statement outside Network": "550 VND",
                    "Cash Withdrawal (Domestic, within Network)": "2,200 VND",
                    "Cash Withdrawal (Domestic, outside Network)": "3,300 VND",
                    "Foreign Currency Transaction Fee": "N/A",
                    "Transfer to Another VIB Account (ATM/POS)": "Free",
                    "Transfer to Another Bank (ATM/POS)": "0.01% (Min 1,100 VND, Max 16,500 VND)"
                },
                "Other Service Fees": {
                    "Card Replacement Fee per transaction": "50,000 VND",
                    "Card Renewal Fee": "Free",
                    "PIN Reissue Fee per transaction": "22,000 VND",
                    "Card Number Selection Fee per transaction": "N/A",
                    "Dispute Fee (Incorrect Transaction)": "N/A",
                    "Express Card Issuance/Replacement Fee per transaction": "110,000 VND",
                    "Special Service Fee per transaction": "500,000 VND"
                }
            }
        }
    # credits
    elif card_type == "VIB Cash Back":
        json_dict = {
            "card_name": "VIB Cash Back",
            "product_type": "credit",
            "highlight-features": {
                "annual_fee": "899,000 VND/year for main card, 599,000 VND/year for supplementary card",
                "reward_rate": "Up to 10% cash back and unlimited reward points",
                "interest": "Interest-free for up to 55 days. From 0.83% to 3.29%/month based on credit history",
                "transactions_per_day": "Not specified"
            },
            "benefit": {
                "is_cashback": True,
                "is_low_interest": False,
                "for_shopping": True,
                "for_food": True,
                "for_entertainment": True,
                "for_insurance": False,
                "for_education": False
            },
            "cashback_limit_per_month": "500,000 VND per customer/30 days",
            "mobile_payment_solutions": ["Internet Banking", "MyVIB", "ATMs nationwide"],
            "fees": {
                "Card Issuance and Maintenance Fees": {
                    "Card Issuance Fee": {
                        "Main Card": "Free",
                        "Supplementary Card (Standard Design)": "110,000 VND",
                        "Supplementary Card (Special Design)": "330,000 VND"
                    },
                    "Card Maintenance Fee per year": "899,000 VND for main card, 599,000 VND for supplementary card"
                },
                "ATM Transaction Fees": {
                    "Balance Inquiry / Statement within Network": "Free",
                    "Balance Inquiry / Statement outside Network": "550 VND",
                    "Cash Withdrawal (Domestic, within Network)": "2,200 VND",
                    "Cash Withdrawal (Domestic, outside Network)": "3,300 VND",
                    "Foreign Currency Transaction Fee": "3% (Min 10,000 VND)",
                    "Vietnamese Currency Transaction Abroad": "1.1% (Min 10,000 VND)",
                    "Transfer to Another VIB Account (ATM/POS)": "Free",
                    "Transfer to Another Bank (ATM/POS)": "0.01% (Min 1,100 VND, Max 16,500 VND)"
                },
                "Other Service Fees": {
                    "Card Replacement Fee per transaction": "200,000 VND",
                    "Card Renewal Fee": "Free",
                    "PIN Reissue Fee per transaction": "50,000 VND",
                    "Card Number Selection Fee": "500,000 VND",
                    "Card Replacement (Lost/Stolen) Fee": "250,000 VND",
                    "Express Card Issuance/Replacement Fee per transaction": "200,000 VND",
                    "Special Service Fee per transaction": "500,000 VND",
                    "Late Payment Fee": "4% of outstanding balance (Min 200,000 VND, Max 2,000,000 VND)",
                    "Overlimit Fee": "4% of overlimit amount per transaction",
                    "Transaction Dispute Fee": "200,000 VND",
                    "Automatic Payment Fee (if not met conditions)": "10,000 VND",
                    "Fee for Credit Limit Increase": "100,000 VND",
                    "Account Statement Reissue Fee": "50,000 VND"
                }
            }
        }
    elif card_type == "VIB Premier Boundless":
        json_dict = {
            "card_name": "VIB Premier Boundless",
            "product_type": "credit",
            "highlight-features": {
                "annual_fee": "1,299,000 VND/year for main card, 699,000 VND/year for supplementary card",
                "reward_rate": "Up to 10% cashback, accumulate miles for all expenses",
                "interest": "Interest-free for up to 55 days. From 0.83% to 3.29%/month based on credit history",
                "transactions_per_day": "Not specified"
            },
            "benefit": {
                "is_cashback": True,
                "is_low_interest": True,
                "for_shopping": True,
                "for_food": False,
                "for_entertainment": True,
                "for_insurance": False,
                "for_education": False
            },
            "cashback_limit_per_month": "500,000 VND per customer/30 days",
            "mobile_payment_solutions": ["Internet Banking", "MyVIB", "ATMs nationwide"],
            "miles_accumulation": {
                "vietnam_airlines": "1 mile per 15,000 VND spent",
                "international_spending": "1 mile per 25,000 VND spent",
                "domestic_spending": "1 mile per 30,000 VND spent"
            },
            "additional_benefits": {
                "airport_lounge_access": "Free lounge access for primary cardholder with spending of 60 million VND/year, or maximum 4 visits per year for both primary and supplementary cardholders",
                "special_discount_at_airport_restaurants": "10%-25% off"
            },
            "referral_program": {
                "bonus_for_successful_referral": {
                "1st": "500,000 VND",
                "3rd": "3,000,000 VND",
                "5th": "6,000,000 VND"
                },
                "bonus_for_exceeding_target": "500,000 VND"
            },
            "fees": {
                "Card Issuance and Maintenance Fees": {
                "Card Issuance Fee": {
                    "Main Card": "Free",
                    "Supplementary Card": "699,000 VND"
                },
                "Card Maintenance Fee per year": "1,299,000 VND for main card, 699,000 VND for supplementary card"
                },
                "ATM Transaction Fees": {
                "Balance Inquiry / Statement within Network": "Free",
                "Balance Inquiry / Statement outside Network": "550 VND",
                "Cash Withdrawal (Domestic, within Network)": "2,200 VND",
                "Cash Withdrawal (Domestic, outside Network)": "3,300 VND",
                "Foreign Currency Transaction Fee": "3% (Min 10,000 VND)",
                "Vietnamese Currency Transaction Abroad": "1% (Min 10,000 VND)",
                "Transfer to Another VIB Account (ATM/POS)": "Free",
                "Transfer to Another Bank (ATM/POS)": "0.01% (Min 1,100 VND, Max 16,500 VND)"
                },
                "Other Service Fees": {
                "Card Replacement Fee per transaction": "200,000 VND",
                "Card Renewal Fee": "Free",
                "PIN Reissue Fee per transaction": "50,000 VND",
                "Card Number Selection Fee": "500,000 VND",
                "Card Replacement (Lost/Stolen) Fee": "250,000 VND",
                "Express Card Issuance/Replacement Fee per transaction": "200,000 VND",
                "Special Service Fee per transaction": "500,000 VND",
                "Late Payment Fee": "4% of outstanding balance (Min 200,000 VND, Max 2,000,000 VND)",
                "Overlimit Fee": "3.5% of overlimit amount per transaction",
                "Transaction Dispute Fee": "200,000 VND",
                "Automatic Payment Fee (if not met conditions)": "10,000 VND",
                "Fee for Credit Limit Increase": "100,000 VND",
                "Account Statement Reissue Fee": "50,000 VND"
                }
            }
        }
    elif card_type == "VIB Travel Élite":
        json_dict = {
            "card_name": "VIB Travel Élite",
            "product_type": "credit",
            "highlight-features": {
                "foreign_transaction_fee": "0% for first 3 statements, 1% thereafter",
                "annual_fee": "1,299,000 VND for main card, 699,000 VND for supplementary card",
                "reward_rate": "Up to 10% cashback, accumulate miles for all expenses",
                "interest": "Interest-free for up to 55 days. From 0.83% to 3.29%/month based on credit history",
                "transactions_per_day": "Not specified"
            },
            "benefit": {
                "is_cashback": True,
                "is_low_interest": True,
                "for_shopping": True,
                "for_food": False,
                "for_entertainment": True,
                "for_insurance": False,
                "for_education": False
            },
            "cashback_limit_per_month": "500,000 VND per customer/30 days",
            "mobile_payment_solutions": ["Internet Banking", "MyVIB", "ATMs nationwide"],
            "miles_accumulation": {
                "vietnam_airlines": "1 mile per 20,000 VND spent abroad",
                "international_spending": "1 mile per 20,000 VND spent",
                "domestic_spending": "1 mile per 30,000 VND spent"
            },
            "additional_benefits": {
                "airport_lounge_access": "Free lounge access for primary cardholder with spending of 60 million VND/year, or maximum 4 visits per year for both primary and supplementary cardholders",
                "special_discount_at_airport_restaurants": "10%-25% off",
                "mastercard_travel_pass": "Access to over 1,300 airport lounges worldwide, with unlimited access for cardholders meeting spending conditions"
            },
            "referral_program": {
                "bonus_for_successful_referral": {
                    "1st": "500,000 VND",
                    "3rd": "3,000,000 VND",
                    "5th": "6,000,000 VND"
                },
                "bonus_for_exceeding_target": "500,000 VND"
            },
            "fees": {
                "Card Issuance and Maintenance Fees": {
                    "Card Issuance Fee": {
                        "Main Card": "Free",
                        "Supplementary Card": "699,000 VND"
                    },
                    "Card Maintenance Fee per year": "1,299,000 VND for main card, 699,000 VND for supplementary card"
                },
                "ATM Transaction Fees": {
                    "Balance Inquiry / Statement within Network": "Free",
                    "Balance Inquiry / Statement outside Network": "550 VND",
                    "Cash Withdrawal (Domestic, within Network)": "2,200 VND",
                    "Cash Withdrawal (Domestic, outside Network)": "3,300 VND",
                    "Foreign Currency Transaction Fee": "1% (Min 10,000 VND)",
                    "Vietnamese Currency Transaction Abroad": "1% (Min 10,000 VND)",
                    "Transfer to Another VIB Account (ATM/POS)": "Free",
                    "Transfer to Another Bank (ATM/POS)": "0.01% (Min 1,100 VND, Max 16,500 VND)"
                },
                "Other Service Fees": {
                    "Card Replacement Fee per transaction": "200,000 VND",
                    "Card Renewal Fee": "Free",
                    "PIN Reissue Fee per transaction": "50,000 VND",
                    "Card Number Selection Fee": "500,000 VND",
                    "Card Replacement (Lost/Stolen) Fee": "250,000 VND",
                    "Express Card Issuance/Replacement Fee per transaction": "200,000 VND",
                    "Special Service Fee per transaction": "500,000 VND",
                    "Late Payment Fee": "4% of outstanding balance (Min 200,000 VND, Max 2,000,000 VND)",
                    "Overlimit Fee": "3.5% of overlimit amount per transaction",
                    "Transaction Dispute Fee": "200,000 VND",
                    "Automatic Payment Fee (if not met conditions)": "10,000 VND",
                    "Fee for Credit Limit Increase": "100,000 VND",
                    "Account Statement Reissue Fee": "50,000 VND"
                }
            }
        }
    elif card_type == "VIB Rewards Unlimited":
        json_dict = {
                "card_name": "VIB Rewards Unlimited",
                "product_type": "credit",
                "highlight-features": {
                    "foreign_transaction_fee": "3.5% (Min 10,000 VND)",
                    "annual_fee": "499,000 VND for main card, 299,000 VND for supplementary card",
                    "reward_rate": "Up to 10% cashback, accumulate points for all expenses",
                    "interest": "Interest-free for up to 45 days. From 0.83% to 3.29%/month based on credit history",
                    "transactions_per_day": "Not specified"
                },
                "benefit": {
                    "is_cashback": True,
                    "is_low_interest": True,
                    "for_shopping": True,
                    "for_food": False,
                    "for_entertainment": True,
                    "for_insurance": False,
                    "for_education": False
                },
                "cashback_limit_per_month": "500,000 VND per customer/30 days",
                "mobile_payment_solutions": ["Apple Pay", "Google Pay", "Samsung Pay", "Garmin Pay"],
                "miles_accumulation": {
                    "vietnam_airlines": "1 mile per 20,000 VND spent abroad",
                    "international_spending": "1 mile per 20,000 VND spent",
                    "domestic_spending": "1 mile per 30,000 VND spent"
                },
                "additional_benefits": {
                    "airport_lounge_access": "Free lounge access for primary cardholder with spending of 60 million VND/year, or maximum 4 visits per year for both primary and supplementary cardholders",
                    "special_discount_at_airport_restaurants": "10%-25% off",
                    "mastercard_travel_pass": "Access to over 1,300 airport lounges worldwide, with unlimited access for cardholders meeting spending conditions"
                },
                "referral_program": {
                    "bonus_for_successful_referral": {
                    "1st": "500,000 VND",
                    "3rd": "3,000,000 VND",
                    "5th": "6,000,000 VND"
                    },
                    "bonus_for_exceeding_target": "500,000 VND"
                },
                "fees": {
                    "Card Issuance and Maintenance Fees": {
                    "Card Issuance Fee": {
                        "Main Card": "Free",
                        "Supplementary Card": "299,000 VND"
                    },
                    "Card Maintenance Fee per year": "499,000 VND for main card, 299,000 VND for supplementary card"
                    },
                    "ATM Transaction Fees": {
                    "Balance Inquiry / Statement within Network": "Free",
                    "Balance Inquiry / Statement outside Network": "550 VND",
                    "Cash Withdrawal (Domestic, within Network)": "2,200 VND",
                    "Cash Withdrawal (Domestic, outside Network)": "3,300 VND",
                    "Foreign Currency Transaction Fee": "3.5% (Min 10,000 VND)",
                    "Vietnamese Currency Transaction Abroad": "1.1% (Min 10,000 VND)",
                    "Transfer to Another VIB Account (ATM/POS)": "Free",
                    "Transfer to Another Bank (ATM/POS)": "0.01% (Min 1,100 VND, Max 16,500 VND)"
                    },
                    "Other Service Fees": {
                    "Card Replacement Fee per transaction": "200,000 VND",
                    "Card Renewal Fee": "Free",
                    "PIN Reissue Fee per transaction": "50,000 VND",
                    "Card Number Selection Fee": "500,000 VND",
                    "Card Replacement (Lost/Stolen) Fee": "250,000 VND",
                    "Express Card Issuance/Replacement Fee per transaction": "200,000 VND",
                    "Special Service Fee per transaction": "500,000 VND",
                    "Late Payment Fee": "4% of outstanding balance (Min 200,000 VND, Max 2,000,000 VND)",
                    "Overlimit Fee": "3.5% of overlimit amount per transaction",
                    "Transaction Dispute Fee": "200,000 VND",
                    "Automatic Payment Fee (if not met conditions)": "10,000 VND",
                    "Fee for Credit Limit Increase": "100,000 VND",
                    "Account Statement Reissue Fee": "50,000 VND"
                    }
                }
        }
    elif card_type == "VIB Online Plus 2in1":
        json_dict = {
            "card_name": "VIB Online Plus 2in1",
            "product_type": "credit",
            "highlight-features": {
                "foreign_transaction_fee": "3.5% (Min 10,000 VND)",
                "annual_fee": "599,000 VND for main card, 299,000 VND for supplementary card",
                "reward_rate": "Up to 6% cashback for online spending",
                "interest": "Interest-free for up to 55 days. From 0.83% to 3.29%/month based on credit history",
                "transactions_per_day": "Not specified"
            },
            "benefit": {
                "is_cashback": True,
                "is_low_interest": True,
                "for_shopping": True,
                "for_food": False,
                "for_entertainment": False,
                "for_insurance": False,
                "for_education": False
            },
            "cashback_limit_per_month": "500,000 VND per customer/30 days",
            "mobile_payment_solutions": ["Apple Pay", "Google Pay", "Samsung Pay", "Garmin Pay"],
            "miles_accumulation": {
                "vietnam_airlines": "1 mile per 20,000 VND spent abroad",
                "international_spending": "1 mile per 20,000 VND spent",
                "domestic_spending": "1 mile per 30,000 VND spent"
            },
            "additional_benefits": {
                "airport_lounge_access": "Premium lounge access at airports (999,000 VND per visit)",
                "airport_services": {
                "fast_track_checkin": "1,099,000 VND per visit at international airports",
                "airport_pickup_dropoff": "999,000 VND per visit"
                },
                "cash_conversion": "Quick conversion of cashback points into cash or vouchers through MyVIB"
            },
            "referral_program": {
                "bonus_for_successful_referral": {
                "1st": "500,000 VND",
                "3rd": "3,000,000 VND",
                "5th": "6,000,000 VND"
                },
                "bonus_for_exceeding_target": "500,000 VND"
            },
            "fees": {
                "Card Issuance and Maintenance Fees": {
                "Card Issuance Fee": {
                    "Main Card": "Free",
                    "Supplementary Card": "299,000 VND"
                },
                "Card Maintenance Fee per year": "599,000 VND for main card, 299,000 VND for supplementary card"
                },
                "ATM Transaction Fees": {
                "Balance Inquiry / Statement within Network": "Free",
                "Balance Inquiry / Statement outside Network": "550 VND",
                "Cash Withdrawal (Domestic, within Network)": "2,200 VND",
                "Cash Withdrawal (Domestic, outside Network)": "3,300 VND",
                "Foreign Currency Transaction Fee": "3.5% (Min 10,000 VND)",
                "Vietnamese Currency Transaction Abroad": "1.1% (Min 10,000 VND)",
                "Transfer to Another VIB Account (ATM/POS)": "Free",
                "Transfer to Another Bank (ATM/POS)": "0.01% (Min 1,100 VND, Max 16,500 VND)"
                },
                "Other Service Fees": {
                "Card Replacement Fee per transaction": "200,000 VND",
                "Card Renewal Fee": "Free",
                "PIN Reissue Fee per transaction": "50,000 VND",
                "Card Number Selection Fee": "500,000 VND",
                "Card Replacement (Lost/Stolen) Fee": "250,000 VND",
                "Express Card Issuance/Replacement Fee per transaction": "200,000 VND",
                "Special Service Fee per transaction": "500,000 VND",
                "Late Payment Fee": "4% of outstanding balance (Min 200,000 VND, Max 2,000,000 VND)",
                "Overlimit Fee": "4% of overlimit amount per transaction",
                "Transaction Dispute Fee": "200,000 VND",
                "Automatic Payment Fee (if not met conditions)": "10,000 VND",
                "Fee for Credit Limit Increase": "100,000 VND",
                "Account Statement Reissue Fee": "50,000 VND"
                }
            }
            }
    elif card_type == "VIB Family Link":
        json_dict = {
                "card_name": "VIB Family Link",
                "product_type": "credit",
                "highlight-features": {
                    "foreign_transaction_fee": "3% (Min 10,000 VND)",
                    "annual_fee": "499,000 VND for main card, 250,000 VND for supplementary card (if opened and linked within 30 days)",
                    "reward_rate": "Up to 10% cashback on education, healthcare, insurance spending. 5% on up to 50 million VND in eligible spending.",
                    "interest": "Interest-free for up to 55 days. From 0.83% to 3.29%/month based on credit history",
                    "transactions_per_day": "Not specified"
                },
                "benefit": {
                    "is_cashback": True,
                    "is_low_interest": True,
                    "for_shopping": True,
                    "for_food": False,
                    "for_entertainment": False,
                    "for_insurance": True,
                    "for_education": True
                },
                "cashback_limit_per_month": "1,000,000 Smile points per statement cycle",
                "mobile_payment_solutions": ["Apple Pay", "Google Pay", "Samsung Pay"],
                "miles_accumulation": {
                    "vietnam_airlines": "1 mile per 20,000 VND spent abroad",
                    "international_spending": "1 mile per 20,000 VND spent",
                    "domestic_spending": "1 mile per 30,000 VND spent"
                },
                "additional_benefits": {
                    "airport_lounge_access": "Premium lounge access at airports (999,000 VND per visit)",
                    "airport_services": {
                        "fast_track_checkin": "1,099,000 VND per visit at international airports",
                        "airport_pickup_dropoff": "999,000 VND per visit"
                    },
                    "cash_conversion": "Quick conversion of cashback points into cash or vouchers through MyVIB"
                },
                "referral_program": {
                    "bonus_for_successful_referral": {
                        "1st": "500,000 VND",
                        "3rd": "3,000,000 VND",
                        "5th": "6,000,000 VND"
                    },
                    "bonus_for_exceeding_target": "500,000 VND"
                },
                "fees": {
                    "Card Issuance and Maintenance Fees": {
                        "Card Issuance Fee": {
                            "Main Card": "Free",
                            "Supplementary Card": "250,000 VND"
                        },
                        "Card Maintenance Fee per year": "499,000 VND for main card, 250,000 VND for supplementary card"
                    },
                    "ATM Transaction Fees": {
                        "Balance Inquiry / Statement within Network": "Free",
                        "Balance Inquiry / Statement outside Network": "550 VND",
                        "Cash Withdrawal (Domestic, within Network)": "2,200 VND",
                        "Cash Withdrawal (Domestic, outside Network)": "3,300 VND",
                        "Foreign Currency Transaction Fee": "3% (Min 10,000 VND)",
                        "Vietnamese Currency Transaction Abroad": "1.1% (Min 10,000 VND)",
                        "Transfer to Another VIB Account (ATM/POS)": "Free",
                        "Transfer to Another Bank (ATM/POS)": "0.01% (Min 1,100 VND, Max 16,500 VND)"
                    },
                    "Other Service Fees": {
                        "Card Replacement Fee per transaction": "200,000 VND",
                        "Card Renewal Fee": "Free",
                        "PIN Reissue Fee per transaction": "50,000 VND",
                        "Card Number Selection Fee": "500,000 VND",
                        "Card Replacement (Lost/Stolen) Fee": "250,000 VND",
                        "Express Card Issuance/Replacement Fee per transaction": "200,000 VND",
                        "Special Service Fee per transaction": "500,000 VND",
                        "Late Payment Fee": "4% of outstanding balance (Min 200,000 VND, Max 2,000,000 VND)",
                        "Overlimit Fee": "4% of overlimit amount per transaction",
                        "Transaction Dispute Fee": "200,000 VND",
                        "Automatic Payment Fee (if not met conditions)": "10,000 VND",
                        "Fee for Credit Limit Increase": "100,000 VND",
                        "Account Statement Reissue Fee": "50,000 VND"
                    }
                }
        }
    elif card_type == "VIB Financial Free":
        json_dict = {
            "card_name": "VIB Financial Free",
            "product_type": "credit",
            "highlight-features": {
                "foreign_transaction_fee": "3.5% (Min 10,000 VND)",
                "annual_fee": "Free for lifetime. First year and second year free if total POS/Internet transactions reach at least 12 million VND in the first year",
                "reward_rate": "Up to 1,200,000 VND cashback per month for successful referrals",
                "interest": "Interest-free for the first 3 months on all transactions and cash withdrawals. From 0.83% to 3.29%/month based on credit history",
                "transactions_per_day": "Not specified"
            },
            "benefit": {
                "is_cashback": True,
                "is_low_interest": True,
                "for_shopping": True,
                "for_food": False,
                "for_entertainment": False,
                "for_insurance": False,
                "for_education": False
            },
            "cashback_limit_per_month": "1,200,000 VND per card",
            "mobile_payment_solutions": ["Apple Pay", "Google Pay", "Samsung Pay", "Garmin Pay"],
            "miles_accumulation": {
                "vietnam_airlines": "1 mile per 20,000 VND spent abroad",
                "international_spending": "1 mile per 20,000 VND spent",
                "domestic_spending": "1 mile per 30,000 VND spent"
            },
            "additional_benefits": {
                "airport_lounge_access": "Premium lounge access at airports (999,000 VND per visit)",
                "airport_services": {
                    "fast_track_checkin": "1,099,000 VND per visit at international airports",
                    "airport_pickup_dropoff": "999,000 VND per visit"
                },
                "cash_conversion": "Quick conversion of cashback points into cash or vouchers through MyVIB"
            },
            "referral_program": {
                "bonus_for_successful_referral": {
                    "1st": "500,000 VND",
                    "3rd": "3,000,000 VND",
                    "5th": "6,000,000 VND"
                },
                "bonus_for_exceeding_target": "500,000 VND"
            },
            "fees": {
                "Card Issuance and Maintenance Fees": {
                    "Card Issuance Fee": {
                        "Main Card": "Free",
                        "Supplementary Card": "Free"
                    },
                    "Card Maintenance Fee per year": "Free for lifetime (if POS/Internet transactions reach 12 million VND in the previous year)"
                },
                "ATM Transaction Fees": {
                    "Balance Inquiry / Statement within Network": "Free",
                    "Balance Inquiry / Statement outside Network": "550 VND",
                    "Cash Withdrawal (Domestic, within Network)": "Free",
                    "Cash Withdrawal (Domestic, outside Network)": "3,300 VND",
                    "Foreign Currency Transaction Fee": "3.5% (Min 10,000 VND)",
                    "Vietnamese Currency Transaction Abroad": "1.1% (Min 10,000 VND)",
                    "Transfer to Another VIB Account (ATM/POS)": "Free",
                    "Transfer to Another Bank (ATM/POS)": "0.01% (Min 1,100 VND, Max 16,500 VND)"
                },
                "Other Service Fees": {
                    "Card Replacement Fee per transaction": "100,000 VND",
                    "Card Renewal Fee": "Free",
                    "PIN Reissue Fee per transaction": "50,000 VND",
                    "Card Number Selection Fee": "500,000 VND",
                    "Card Replacement (Lost/Stolen) Fee": "250,000 VND",
                    "Express Card Issuance/Replacement Fee per transaction": "200,000 VND",
                    "Special Service Fee per transaction": "500,000 VND",
                    "Late Payment Fee": "6% of outstanding balance (Min 200,000 VND, Max 2,000,000 VND)",
                    "Overlimit Fee": "4.5% of overlimit amount per transaction",
                    "Transaction Dispute Fee": "200,000 VND",
                    "Automatic Payment Fee (if not met conditions)": "10,000 VND",
                    "Fee for Credit Limit Increase": "100,000 VND",
                    "Account Statement Reissue Fee": "50,000 VND"
                }
            }
        }
    elif card_type == "VIB LazCard":
        json_dict = {
            "card_name": "VIB LazCard",
            "product_type": "credit",
            "highlight-features": {
                "foreign_transaction_fee": "3% (Min 10,000 VND)",
                "annual_fee": "599,000 VND per year",
                "reward_rate": "Up to 6% cashback on Lazada purchases, 3% on other online transactions, 0.1% on other purchases",
                "interest": "Interest-free for up to 55 days on purchases. From 0.83% to 3.29%/month based on credit history",
                "transactions_per_day": "Not specified"
            },
            "benefit": {
                "is_cashback": True,
                "is_low_interest": True,
                "for_shopping": True,
                "for_food": False,
                "for_entertainment": False,
                "for_insurance": False,
                "for_education": False
            },
            "cashback_limit_per_month": "500,000 VND per month for cashback",
            "mobile_payment_solutions": ["Apple Pay", "Google Pay", "Samsung Pay", "Garmin Pay"],
            "miles_accumulation": {
                "vietnam_airlines": "Not specified",
                "international_spending": "Not specified",
                "domestic_spending": "Not specified"
            },
            "additional_benefits": {
                "airport_lounge_access": "Premium lounge access at airports (999,000 VND per visit)",
                "airport_services": {
                    "fast_track_checkin": "1,099,000 VND per visit at international airports",
                    "airport_pickup_dropoff": "999,000 VND per visit"
                },
                "cash_conversion": "Quick conversion of cashback points into cash or vouchers through MyVIB"
            },
            "referral_program": {
                "bonus_for_successful_referral": {
                    "1st": "500,000 VND",
                    "3rd": "3,000,000 VND",
                    "5th": "6,000,000 VND"
                },
                "bonus_for_exceeding_target": "500,000 VND"
            },
            "fees": {
                "Card Issuance and Maintenance Fees": {
                    "Card Issuance Fee": {
                        "Main Card": "Free",
                        "Supplementary Card": "299,000 VND"
                    },
                    "Card Maintenance Fee per year": "599,000 VND (first year free with spending of 1,000,000 VND)"
                },
                "ATM Transaction Fees": {
                    "Balance Inquiry / Statement within Network": "Free",
                    "Balance Inquiry / Statement outside Network": "550 VND",
                    "Cash Withdrawal (Domestic, within Network)": "Free",
                    "Cash Withdrawal (Domestic, outside Network)": "3,300 VND",
                    "Foreign Currency Transaction Fee": "3% (Min 10,000 VND)",
                    "Vietnamese Currency Transaction Abroad": "1.1% (Min 10,000 VND)",
                    "Transfer to Another VIB Account (ATM/POS)": "Free",
                    "Transfer to Another Bank (ATM/POS)": "0.01% (Min 1,100 VND, Max 16,500 VND)"
                },
                "Other Service Fees": {
                    "Card Replacement Fee per transaction": "200,000 VND",
                    "Card Renewal Fee": "Free",
                    "PIN Reissue Fee per transaction": "50,000 VND",
                    "Card Number Selection Fee": "500,000 VND",
                    "Card Replacement (Lost/Stolen) Fee": "250,000 VND",
                    "Express Card Issuance/Replacement Fee per transaction": "200,000 VND",
                    "Special Service Fee per transaction": "500,000 VND",
                    "Late Payment Fee": "4% of outstanding balance (Min 200,000 VND, Max 2,000,000 VND)",
                    "Overlimit Fee": "4% of overlimit amount per transaction",
                    "Transaction Dispute Fee": "200,000 VND",
                    "Automatic Payment Fee (if not met conditions)": "10,000 VND",
                    "Fee for Credit Limit Increase": "100,000 VND",
                    "Account Statement Reissue Fee": "50,000 VND"
                }
            }
        }
    elif card_type == "VIB Ivy Card":
        json_dict = {
            "card_name": "VIB Ivy Card",
            "product_type": "credit",
            "highlight-features": {
                "foreign_transaction_fee": "3% (Min 10,000 VND)",
                "annual_fee": "Free for the first year. Free for the second year if POS/Internet transactions reach at least 12 million VND in the first year",
                "reward_rate": "1% cashback on all spending",
                "interest": "Interest-free for up to 45 days on purchases. From 0.83% to 3.29%/month based on credit history",
                "transactions_per_day": "Not specified"
            },
            "benefit": {
                "is_cashback": True,
                "is_low_interest": True,
                "for_shopping": True,
                "for_food": False,
                "for_entertainment": False,
                "for_insurance": False,
                "for_education": False
            },
            "cashback_limit_per_month": "500,000 VND per statement period",
            "mobile_payment_solutions": ["Apple Pay", "Google Pay", "Samsung Pay", "Garmin Pay"],
            "miles_accumulation": {
                "vietnam_airlines": "Not specified",
                "international_spending": "Not specified",
                "domestic_spending": "Not specified"
            },
            "additional_benefits": {
                "airport_lounge_access": "Premium lounge access at airports (999,000 VND per visit)",
                "airport_services": {
                    "fast_track_checkin": "1,099,000 VND per visit at international airports",
                    "airport_pickup_dropoff": "999,000 VND per visit"
                },
                "cash_conversion": "Quick conversion of cashback points into cash or vouchers through MyVIB"
            },
            "referral_program": {
                "bonus_for_successful_referral": {
                    "1st": "500,000 VND",
                    "3rd": "3,000,000 VND",
                    "5th": "6,000,000 VND"
                },
                "bonus_for_exceeding_target": "500,000 VND"
            },
            "fees": {
                "Card Issuance and Maintenance Fees": {
                    "Card Issuance Fee": {
                        "Main Card": "Free",
                        "Supplementary Card": "Free"
                    },
                    "Card Maintenance Fee per year": "299,000 VND (Free for the first year, free for the second year if 12 million VND spending is met in the first year)"
                },
                "ATM Transaction Fees": {
                    "Balance Inquiry / Statement within Network": "Free",
                    "Balance Inquiry / Statement outside Network": "550 VND",
                    "Cash Withdrawal (Domestic, within Network)": "Free",
                    "Cash Withdrawal (Domestic, outside Network)": "3,300 VND",
                    "Foreign Currency Transaction Fee": "3% (Min 10,000 VND)",
                    "Vietnamese Currency Transaction Abroad": "1.1% (Min 10,000 VND)",
                    "Transfer to Another VIB Account (ATM/POS)": "Free",
                    "Transfer to Another Bank (ATM/POS)": "0.01% (Min 1,100 VND, Max 16,500 VND)"
                },
                "Other Service Fees": {
                    "Card Replacement Fee per transaction": "100,000 VND",
                    "Card Renewal Fee": "Free",
                    "PIN Reissue Fee per transaction": "50,000 VND",
                    "Card Number Selection Fee": "500,000 VND",
                    "Card Replacement (Lost/Stolen) Fee": "250,000 VND",
                    "Express Card Issuance/Replacement Fee per transaction": "200,000 VND",
                    "Special Service Fee per transaction": "500,000 VND",
                    "Late Payment Fee": "4% of outstanding balance (Min 50,000 VND, Max 300,000 VND)",
                    "Overlimit Fee": "4% of overlimit amount per transaction",
                    "Transaction Dispute Fee": "200,000 VND",
                    "Automatic Payment Fee (if not met conditions)": "10,000 VND",
                    "Fee for Credit Limit Increase": "100,000 VND",
                    "Account Statement Reissue Fee": "50,000 VND"
                }
            }
        }
    elif card_type == "VIB Super Card":
        json_dict ={
            "card_name": "VIB Super Card",
            "product_type": "credit",
            "highlight_features": {
                "foreign_transaction_fee": "3% (Min 10,000 VND)",
                "annual_fee": "999,000 VND",
                "reward_rate": "15% for shopping, travel, and dining, 10% for online and foreign transactions, 0.1% for other spending",
                "interest": "Interest-free for up to 55 days on purchases. From 0.83% to 3.29%/month based on credit history",
                "transactions_per_day": "Not specified"
            },
            "benefit": {
                "is_cashback": True,
                "is_low_interest": True,
                "for_shopping": True,
                "for_food": True,
                "for_entertainment": False,
                "for_insurance": False,
                "for_education": False
            },
            "cashback_limit_per_month": "500,000 VND per statement period",
            "mobile_payment_solutions": ["Apple Pay", "Google Pay", "Samsung Pay", "Garmin Pay"],
            "miles_accumulation": {
                "vietnam_airlines": "Not specified",
                "international_spending": "10% reward points",
                "domestic_spending": "15% reward points"
            },
            "additional_benefits": {
                "airport_lounge_access": "Premium lounge access at airports (999,000 VND per visit)",
                "airport_services": {
                    "fast_track_checkin": "1,099,000 VND per visit at international airports",
                    "airport_pickup_dropoff": "999,000 VND per visit"
                },
                "cash_conversion": "Quick conversion of reward points into cash or vouchers through MyVIB"
            },
            "referral_program": {
                "bonus_for_successful_referral": {
                    "1st": "500,000 VND",
                    "3rd": "3,000,000 VND",
                    "5th": "6,000,000 VND"
                },
                "bonus_for_exceeding_target": "500,000 VND"
            },
            "fees": {
                "Card Issuance and Maintenance Fees": {
                    "Card Issuance Fee": {
                        "Main Card": "Free",
                        "Supplementary Card": "499,000 VND"
                    },
                    "Card Maintenance Fee per year": "999,000 VND"
                },
                "ATM Transaction Fees": {
                    "Balance Inquiry / Statement within Network": "Free",
                    "Balance Inquiry / Statement outside Network": "550 VND",
                    "Cash Withdrawal (Domestic, within Network)": "Free",
                    "Cash Withdrawal (Domestic, outside Network)": "3,300 VND",
                    "Foreign Currency Transaction Fee": "3% (Min 10,000 VND)",
                    "Vietnamese Currency Transaction Abroad": "1.1% (Min 10,000 VND)",
                    "Transfer to Another VIB Account (ATM/POS)": "Free",
                    "Transfer to Another Bank (ATM/POS)": "0.01% (Min 1,100 VND, Max 16,500 VND)"
                },
                "Other Service Fees": {
                    "Card Replacement Fee per transaction": "200,000 VND",
                    "Card Renewal Fee": "Free",
                    "PIN Reissue Fee per transaction": "50,000 VND",
                    "Card Number Selection Fee": "500,000 VND",
                    "Card Replacement (Lost/Stolen) Fee": "250,000 VND",
                    "Express Card Issuance/Replacement Fee per transaction": "200,000 VND",
                    "Special Service Fee per transaction": "500,000 VND",
                    "Late Payment Fee": "4% of outstanding balance (Min 200,000 VND, Max 2,000,000 VND)",
                    "Overlimit Fee": "4% of overlimit amount per transaction",
                    "Transaction Dispute Fee": "200,000 VND",
                    "Automatic Payment Fee (if not met conditions)": "10,000 VND",
                    "Fee for Credit Limit Increase": "100,000 VND",
                    "Account Statement Reissue Fee": "50,000 VND"
                }
            }
        }        
    else:
        json_dict = {}    
            
    return json_dict

def get_credit_cards_CoT():
    CoT_sample_prompt = """
        Mục đích là cung cấp thẻ phù hợp với yêu cầu khách hàng, tránh cung cấp mấy cái ngu rồi phán thẻ đó không phù hợp        
        Chain of Thought:
            1. Check the conditions for card issuance (whether there are any cards that do not meet the income requirements) and exclude any ineligible cards.
            2. Remove cards that do not meet the income and credit history conditions, and among the remaining cards, identify those that meet the supplementary features requirements.
            3. Among the cards from step 2, identify the most suitable card.
        Chain of Thought examples:
            <example_1>
                user: Suppose my average income is 18 million VND and I spend around 10 million VND monthly on travel, so which card should I use?
                BOT:
                    <CoT>
                        Step 1. With an income of 18 million VND/month, cards that require an "average minimum income over the last 3 months" in the range of 7-10 million VND are suitable, such as:
                            VIB Cash Back, VIB Reward Unlimited, etc.
                        Cards NOT RECOMMENDED: "VIB Premier Boundless", "VIB Travel Elite" (because these cards require a minimum of 20 million VND in income over the last 3 months).
                        Step 2. So, among the 8 remaining cards, which ones are suitable? Cards that offer benefits like cash back, reward point conversion, etc., will be the most suitable.
                        Step 3. Conclusion: VIB Cash Back.
                    </CoT>
                    <response>
                        Explain why VIB Cash Back is a reasonable choice for the customer (without printing the CoT result above).
                    </response>
            </example_1>
            <example_2>
                user: My income is about 12 million VND, which credit cards I can use?
                BOT:
                    <CoT>
                        Step 1. Among all types of credit cards, only 8 require an average income of the last 3 months below 20 million, which are:
                            VIB Cash Back, VIB Reward Unlimited, etc.
                        Step 2. Among the 8 types above, focus on the minimum income, credit limit, and standout features.
                        Step 3. Suggest the VIB Cashback to them and ask if they would like to know more about the specific features of other cards.                         
                    </CoT>
                    <response>
                        Suggest the VIB Cashback to them and ask if they would like to know more about the specific features of other cards.
                    </response>
            </example_2>
        When responding, only show the final <response> part and do not display the CoT section in the OUTPUT
    """
    return CoT_sample_prompt

def get_poem68_examples():
    poem_samples = """
        <example_01>
            user: "bài thơ thể lục bát tả buổi chiều."
            answer: {{"thể loại": "lục bát", "sample": "Hôm nay trời nhẹ lên cao. Tôi buồn không hiểu vì sao tôi buồn"}}
        </example_01>    
        <example_02>
            user: "bài thơ thể lục bát cảm thán sự đời"
            answer: {{"thể loại": "lục bát", "sample": "Trăm năm trong cõi người ta. Chữ tài chữ mệnh khéo là ghét nhau"}}
        </example_02>
        <example_03>
            user: "thơ lục bát tả nỗi buồn"
            answer: {{"thể loại": "lục bát", "sample": "Buồn nào rồi cũng sẽ xong. Mà sao tôi vẫn cứ rong ruổi hoài. Dẫu biết rằng nỗi khổ chẳng dài. Nhưng lòng vẫn mãi đợi ngày yên vui."}}
        </example_03>
    """
    
    return poem_samples

def get_poem7w_examples():
    poem_samples = """
        <example_01>
            user: "thất ngôn tự tình"
            answer: {{"thể loại": "thất ngôn", "sample": "Tôi đã yêu em từ dạo ấy. Cái chiều hiu hắt gió công viên. Khung trời nhẹ giăng màn nắng nhạt. Hôm ấy đầu xuân, rất nhẹ nhàng"}}
        </example_01>
        <example_02>
            user: "thất ngôn kiêu ngạo lúc ra đi"
            answer: {{"thể loại": "thất ngôn", "sample": "Cất bước ra đi đừng ngoảnh lại. Thẹn với trời xanh, nợ tháng ngày"}}
        </example_02>
        <example_03>
            user: "thơ thất ngôn tương tư 1"
            answer: {{"thể loại": "thất ngôn", "sample": "Xa xăm hờ hững tóc em bay. Dáng người be bé, khuất cỏ cây. Rượu uống vạn ly, ta vẫn tỉnh. Chung trà em rót, thoáng đã say."}}
        </example_03>
        <example_04>
            user: "thơ thất ngôn kẻ si tình ngày tết"
            answer: {{"thể loại": "thất ngôn", "sample": "Mai vàng đơn sắc rơi từng cánh. Hỡi nàng phương ấy đến từ đâu. Mùa xuân đâu phải mùa cô quạnh. Hỡi kẻ si tình khắp thế gian."}}
        </example_04>                
        <example_05>
            user: "thất ngôn tương tư 2"
            answer: {{"thể loại": "thất ngôn", "sample": "Thao thức nhìn trăng với trời mây. Gió xuân thoáng đãng nhẹ mây bay. Hoa trắng nhẹ rơi vào lọn tóc. Khóe mắt tan dần một cõi say"}}
        </example_05>
    """
    
    return poem_samples

def get_freestyle_poem_samples():
    poem_samples = """
        <example_01>
            user: "Thơ tự do suy tư"
            answer: {{"thể loại": "tự do", "sample": "Muôn trùng nắng hạ trong tầm mắt. Điểm một nhành hoa thoáng má hồng. Khung trời đang nhạt màu năm tháng. Nếu ngược thời gian, liệu có còn"}}
        </example_01>    
        <example_02>
            user: "thơ tự do hoài niệm tuổi trẻ"
            answer: {{"thể loại": "tự do", "sample": "Cõi đơn phương, tình như một giấc mộng. Gió đêm về, bất chợt thấy bâng khuân. Trời cao ấy, đã bao lần tuổi trẻ. Nắm cơ đồ, nhưng lại mất tuổi xanh"}}
        </example_02>
    """
    
    return poem_samples    

def story_teller_examples():
    samples = """
            <example_01>
                user: "hãy kể cho tôi một truyện ngắn kinh dị chủ đề thời gian"
                answer: {{"thể loại": "truyện ngắn kinh dị", "sample": "một ngày nọ, tôi tỉnh giấc và thấy 5h sáng. Tôi chợp mắt một chút, 2h sáng, quái lạ. Làm cái đéo gì mà tôi chợp mắt một chút lại trôi qua cả ngày thế này. Hoàn hồn tôi lao ra khỏi giường; đồng hồ chỉ 1h:59 ngày 30/02"}}
            </example_01>
            <example_02>
                user: "hãy kể cho tôi một truyện ngắn kinh dị"
                answer: {{"thể loại": "truyện ngắn kinh dị", "sample": "một đứa trẻ vừa tỉnh dậy sau một giấc ngủ dài, nó kể rằng nó mơ thấy khi nó sinh ra thì nó là một ông lão. Bố mẹ nó an ủi và bố nó được bác sĩ kêu ra nói rằng: bố anh bị đãng trí rồi, ông ấy không biết rằng đã 200 năm qua mọi người đều trẻ hóa khi già đi"}}
            </example_02>
            <example_03>
                user: "hãy kể cho tôi một truyện ngắn kinh dị về mèo"
                answer: {{"thể loại": "truyện ngắn kinh dị", "sample": "Con mèo nhỏ của tôi liên tục cào vào cửa đêm qua khiến tôi không ngủ được. Sáng nay tôi đến mộ của nó với một ít pate và dặn nó đừng vào nhà buổi tối nữa"}}
            </example_03>
            <example_04>
                user: "hãy kể cho tôi một truyện ngắn kinh dị liên quan đến chó"
                answer: {{"thể loại": "truyện ngắn kinh dị", "sample": "Con chó liên tục sủa và nhìn về tôi mỗi đêm. Đêm nay cũng thế, và hình như nó hướng về một cái gì đó sau lưng của tôi"}}
            </example_04>
            <example_05>
                user: "hãy kể cho tôi một truyện ngắn kinh dị chung cư"
                answer: {{"thể loại": "truyện ngắn kinh dị", "sample": "Sau một chầu nhậu bí tỉ với lũ bạn chó chết, tôi trở về căn chung cư ở tầng 29 của mình ngủ thiếp đi. Đột nhiên tôi cảm thấy có ai đó đang gõ cửa. Địt ngựa, âm thanh đó đến từ cửa sổ"}}
            </example_05>
            <example_06>
                user: "truyện cười FPT"
                answer: {{"thể loại": "truyện cười", "sample": "Một nhân viên nhà ép hỏi vị lãnh đụt đáng kính: vì sao cty chúng ta đặt là FPT. Sếp: em đéo học lịch sử cty à? Nhân viên: Lịch sử FPT có cái đéo gì phải học? Sếp: FPT có nghĩa là Fải Phát Triển. Nhân viên: vậy nếu cty khó khăn vỡ nợ ko cứu vãn được thì làm đéo gì? Sếp trầm ngâm hồi lâu rồi phán: Fải Phắng Thôi"}}
            </example_06>
            <example_07>
                user: "truyện cười muôn thú"
                answer: {{"thể loại": "truyện cười", "sample": "Ở một cánh rừng nọ, lạc đà đi lạc đến gặp voi đang uống nước. Thấy con voi to béo đang nhúng vòi xuống suối, lạc đà bèn chửi: đồ cu mọc ngay mõm. Voi cũng không vừa ý và chửi lại: đỡ hơn thằng biến thái vú mọc trên lưng"}}
            </example_07>
            <example_08>
                user: "truyện cười kinh dị"
                answer: {{"thể loại: "truyện cười kinh dị", "sample": "một đêm nọ, người trực mộ đi trong nghĩa địa để dọn lá thì thấy một ông cụ ngồi miệt mài đục đẽo và chùi chùi một ngôi mộ. Người quản trang thấy vậy liền nói: đã khuya rồi sao cụ không về mà ở đây làm gì? Ông cụ quay lại nở một nụ cười bí hiểm: tụi mày khắc sai tên tao nên tao ngồi sửa nè"}}
            </example_08>
            <example_09>
                user: "câu truyền cảm hứng trong EN"
                answer: {{"thể loại": "truyền cảm hứng - động lực", "sample": "Future wont depend on the past, it depends on the passion only"}}
            </example_09>
            <example_10>
                user: "hãy kể cho tôi một truyện ngắn kinh dị chủ đề Nam cực và ăn thịt người"
                answer: {{"thể loại": "truyện ngắn kinh dị", "sample": "Tôi trở về nhà sau một ngày làm việc căng thẳng và vợ tôi đang chuẩn bị đồ ăn trong bếp, cô ấy bảo đó là thịt chim cánh cụt. Nhưng kỳ lạ thay, mùi vị này không hề giống với lần tôi đã thám hiểm dưới nam cực tháng trước. Lần đó, cả đoàn chúng tôi gặp nạn, tôi đói lả người và ngất đi. Khi tỉnh lại thấy những người khỏe mạnh đang chia sẻ với nhau những miếng thịt chim cánh cụt sau chuyến đi săn từ những người còn khỏe. Nhưng lần này tôi ăn hoàn toàn khác, nhưng gượm đã, sao đoàn của chúng tôi khi trở về vẫn thiếu 2 người nhỉ."}}
            </example_10>
            <example_11>
                user: "hãy kể cho tôi một truyện ngắn kinh dị chủ đề hoang mạc"
                answer: {{"thể loại": "truyện ngắn kinh dị", "sample": "Trên một cồn cát ở hoang mạc, tôi và 2 người khác đang chạy trốn một số sinh vật kỳ lạ và lạc đến một ốc đảo. Tại đó chúng tôi được tiếp đãi rất ân cần, những món ăn phong phú, sự nhiệt tình bất kể ngôn ngữ. Khi chúng tôi đã phục hồi và chuẩn bị tạm biệt mọi người, họ lại đãi chúng tôi rất nồng hậu nhưng 2 người bạn của tôi đã say mèm còn tôi thì không uống được nhiều và cũng có nhờ bạn mình uống giúp. Đêm hôm đó, do không say nên tôi tỉnh táo hơn bạn mình và nửa đêm tôi lại nghe thấy tiếng mài dao và âm thanh của những sinh vật đang săn lùng chúng tôi"}}
            </example_11>
            <example_12>
                user: "hãy kể cho tôi một truyện ngắn kinh dị chủ đề sa mạc"
                answer: {{"thể loại": "truyện ngắn kinh dị", "sample": "Tôi tỉnh dậy giữa sa mạc, không nhớ gì về cách mình đến đây. Trong cơn khát cháy cổ, tôi tìm thấy một nguồn nước, nhưng mỗi lần uống, tôi lại thấy mình bị theo dõi bởi những bóng đen lạ. Bầu trời đột nhiên tối sầm, và tôi nghe thấy tiếng bước chân lạ, càng lúc càng gần. Khi quay lại, tôi nhận ra những bóng đen đó không phải người, mà là những con mắt khổng lồ đang bò lúc nhúc và dõi theo tôi từ dưới lớp cát."}}
            </example_12>        
            <example_13>
                user: "hãy kể cho tôi một truyện ngắn kinh dị chủ đề sa mạc và những cái bóng"
                answer: {{"thể loại": "truyện ngắn kinh dị", "sample": "Tôi bước vào một sa mạc hoang vắng, nhưng khi tôi nhìn lại, mọi dấu vết của hành trình đều biến mất. Cát bắt đầu cựa quậy, rồi bỗng dưng tôi thấy những bóng người đang di chuyển trong đó, như thể họ bị mắc kẹt trong lòng đất. Khi tôi chạy, tôi nghe thấy tiếng gọi tên mình, từ chính những cái bóng ấy, vang lên từng lúc một, khiến tôi không thể thoát khỏi. Tôi nhận ra mình không phải là người duy nhất bị lạc trong sa mạc này – tôi đã trở thành một phần của nó."}}
            </example_13>
            <example_14>
                user: "hãy kể cho tôi một truyện ngắn kinh dị chủ đề hoang mạc và những đôi mắt"
                answer: {{"thể loại": "truyện ngắn kinh dị", "sample": "Giữa sa mạc, tôi bắt đầu thấy những lỗ nhỏ kỳ lạ trên mặt cát, chúng mở ra từng chút một như những miệng hố đang thở. Khi tôi bước đến gần, một mùi hôi thối kỳ lạ bốc lên từ dưới cát, như có hàng ngàn con vật nhầy nhụa đang chui ra. Tôi nhìn xuống, và ngay lập tức, những đôi mắt sáng quắc đầy khát máu nhìn chằm chằm lên tôi từ trong những lỗ đó. Cảm giác ghê rợn ập đến khi tôi nhận ra, tôi không phải là sinh vật duy nhất trong sa mạc này."}}
            </example_14>
            <example_15>
                user: "hãy cường điệu trào phúng nghề nghiệp của những kẻ thích sống ảo, phông bạt"
                answer: {{"thể loại": "truyện cười", "sample": "- karaoke tay vịn: ca sĩ hót và nhảy theo giờ \- bán vàng mã đồ cúng: tài chính tâm linh \- cá độ bóng dá: chuyên viên phân tích dữ liệu thể thao \- xuất khẩu lao đông: việt kiều \- bốc vác, phụ hồ: logistc streaming manuscript vật liệu xây dựng \- hút bể phốt, thông cống: chuyên gia xử lý các mỏ khí CH4 tự nhiên \- người mẫu đi khách: kỹ thuật viên sức khỏe sinh lý kiêm trải nghiệm dịch vụ sinh học \- sugar baby: cộng tác viên tâm sinh lý và chuyên gia quản lý tài chính \- sugar daddy: nhà đầu tư tài chính lẫn tình cảm cho các dự án sinh lý \- cảnh sát giao thông: là những con chó dại lông vàng giỏi ngụy trang dưới lớp pikachu khi bị đấm, đi thổi kèn mút sáo cho mọi nhà, thỉnh thoảng đánh giá sức khỏe, đôi lúc còn ăn xin nước bọt và phân phối biên bản cho những vùng sâu vùng xa và vùng kín của đĩ"}}
            </example_15>
            <example_16>
                user: "Hãy châm biếm tên Tô Lâm cục công an"
                answer: {{"thể loại": "truyện cười", "sample": "Ngày xửa ngày xưa, ở làng Đổn có 1 ông bụt trưởng cục Công Ăn, khi vừa mới đẻ mặt rất fuck hậu (môn), Đẻ xong mẹ thằng cún Lâm và cả họ bị thâm lồn nên đặt tên là Tô Thâm Lồn. Sau này lớn lên đi học bị bạn bè dị nghị đặt điều nên ngại ngùng bực tức. Sau lớn lên được điều về xứ thiên đường làm chính trị, từ đó thay tên đổi họ với cái bí danh Tô Dâm, Tô Lông, Tô Lồn và khi về già lấy tên là Tô Lâm. Sau khi lên ngôi, hắn đặt ra rất nhiều điều luật cho đám chó vàng cục giao thông được tự do thổi kèn mút sáo trong khi con dân gầy trơ xương than trời vẫn bị hút không còn một giọt sinh khí. Một ngày nọ, họ Tô ăn phải cứt khi bị ám sát lúc đang đi đái, từ đó đàn chó vàng mất chủ ra đường hửi đít xe, có lần một bầy cún vàng nài nỉ xe tải cán chết bà cả lò tụi nó vì muốn sớm được siêu thoát."}}
            </example_16>
            <example_17>
                user: "truyện kinh dị về công an"
                answer: {{"thể loại": "truyện ngắn kinh dị", "sample": "Một tối nọ, một thằng lồn công an giao thông tan làm về nhưng cả nhà nó đều ngó lơ nó, nó có nói hoài cũng đéo ai care. Bực bội nó về phòng và xem TV. Truyền hình khi đó phát bản tin: sau nghị địt 168, các vụ TNGT có xu hướng giảm nhưng mấy ngày gần đây lại tăng với các nạn nhân là CSGT, riêng hôm nay xảy ra một tai nạn thảm khốc của một đồng chí bị xe tải cán đứt đôi. Thằng lồn đó tặt lưỡi lại một thằng ngu sau đó gương mặt trở nên hốt hoảng khi nhận ra chính nó đang trong bản tin."}}
            </example_17>
            <example_18>
                user: "truyện vui về ông đầu trọc hay hỏi"
                answer: {{"thể loại": "truyện cười", "sample": "Trong một buổi họp, các kỹ sư IT nói với ông senior: bọn em bó tay với mấy yêu cấu quái gỡ của anh rồi. Ông senior gà gãi gãi rồi trả lời: anh cũng bạc đầu với tụi bây rồi đấy. Ở dưới có tiếng xì xầm: anh có tóc đéo đâu mà bạc xỉu với đen đá"}}
            </example_18>
            <example_19>
                user: "truyện cười khoa học cộng sản"
                answer: {{"thể loại": "truyện cười", "sample": "Tại một trại cải tạo các tù nhân chống Cộng, một giáo sư cộng sản bụng phệ, gian dâm vừa đi vừa nói: Như các đồng chí đã biết, tụi tư bản chỉ cho người lên được mặt trăng đã nhảy cẩng lên như chó rồi. Còn CS chúng ta có cái gì, chúng ta còn đưa người lên lấy mẫu đât từ mặt trời. Ở dưới cười ồ lên, vị giáo sư liền tiếp: trí tuệ các người chỉ được đến đây, tôi biết mặt trời nóng cả nghìn độ nên các nhà khoa học chúng tôi chỉ lên đó vào ban đêm khi nó đã nguội. Lúc này ở dưới cười sặc sụa và nhạo: CS các ông là một Cục Shit, ngu như v cũng làm khoa học được, chó nó tin!"}}
            </example_19>
            <example_20>
                user: "truyện cười công nghệ về zip - unzip"
                answer: {{"thể loại": "truyện cười", "sample": "Trong một tiết học, 1 sinh viên học ngu và cá biệt hỏi một giáo sư: quy trình biến một con bò thành cây xúc xích là zip, thế làm cách nào để unzip nó hả GS? Vị GS điềm đạm đáp rằng: năm nay em bao nhiêu tuổi. SV: 19 . GS tiếp: Gần 20 năm trước, bố em đã thực hiện thành công việc unzip với cây xúc xích đó và 9 tháng sau chúng ta có một con bò"}}
            </example_20>
            <example_21>
                user: "ông tổ nói lái châm biếm xứ thiên đàng"
                answer: {{"thể loại": "truyện cười", "sample": "Ở một vương quốc nọ, có thằng vua hách dịch tên Ôn Cắn Lài và một tể tướng có khả năng kinh bang tế sống tên Lời Như Chồn cùng nhau xây dựng một xã hội trong sạch, không một miếng rác vì lúc nào ai ai trong triều đình cũng xung phong Nhặc Cư. Một ngày nọ, vị vua đến làng Đổn, một ngôi làng có truyền thống điều trị giải tỏa tâm lý cao cấp và gặp cô thôn nữ tên Lôn Thị Lầm, ả ta ở làng Côn Ăn chuyên làm nghề đào vàng, ở đó nuôi rất nhiều con chó đực màu vàng đi đâu cũng được kêu cục zàng dẻo nặng mùi. Sau đó thằng Chồn và con Lầm ngoại tình, thằng vua Ôn tức quá xử chém cả 2. Sau đó để tưởng nhớ 2 thánh Lầm và Chồn, nhân dân làng Đổn đã xây tượng đài Con Chồn đi Lạc "}}
            </example_21>
            <example_22>
                user: "truyện kinh dị tủ quần áo trẻ con"
                answer: {{"thể loại": "truyện ngắn kinh dị", "sample": "Khi còn nhỏ, tôi có một người bạn tưởng tượng sống trong tủ quần áo cũ. Một lần, tôi kể với bố về cậu bé đó và vẽ hình cho ông xem. Gương mặt bố tái mét, rồi ngay hôm sau, ông cùng chú tôi đốt cháy cái tủ. Sau này tôi mới biết, chú tôi cũng từng có một người bạn tưởng tượng y hệt, sống trong chính cái tủ đó."}}
            </example_22>
            <example_23>
                user: "truyện về người treo cổ"
                answer: {{"thể loại": "truyện ngắn kinh dị", "sample": "Vào kỳ nghỉ đông 5 năm trước, tôi thấy em họ April, 4 tuổi, ngồi ở chân cầu thang bắt chước biểu cảm của ai đó. Khi hỏi, con bé nói đang làm mặt giống cô thắt bím tóc ở lan can cầu thang. Tôi nhìn quanh chẳng thấy ai, nhưng lúc bước lên, con bé nói: Bím tóc của cô ấy quấn quanh cổ. Vẻ mặt nó đang làm chính là của một người bị ngạt thở."}}
            </example_23>
            <example_24>
                user: "truyện búp bê ma ám"
                answer: {{"thể loại": "truyện ngắn kinh dị", "sample": "Tôi từng làm việc ở điền trang Myrtles, nơi nổi tiếng là ma ám. Có một căn phòng chứa đầy búp bê gốm sứ, trong đó có con búp bê từng thuộc về con gái chủ nhà cũ và nằm trên giường cùng cô bé khi cô qua đời.  Một lần, vị khách di chuyển con búp bê để ngủ thoải mái hơn. Sáng hôm sau, con búp bê trở lại giường với bàn tay đặt lên cổ cô ấy. Một lần khác, khách nghe thấy tiếng gõ nhẹ trong đêm và tỉnh dậy thấy con búp bê ở đúng nơi phát ra âm thanh đó."}}
            </example_24>
            <example_25>
                user: "grandpa"
                answer: {{"thể loại": "truyện ngắn kinh dị", "sample": "Ông tôi mất khi con trai tôi chỉ mới một tuổi. Ông thường làm mặt kỳ lạ để chọc thằng bé cười. Vài đêm sau đám tang, lúc 2 giờ sáng, tôi thấy con trai ngồi giữa phòng khách tối, cười không ngừng. Khi bế nó về phòng, thằng bé thổi một nụ hôn gió vào khoảng không và khúc khích: Tạm biệt papa!"}}
            </example_25>
            <example_26>
                user: "ngón tay bí ẩn"
                answer: {{"thể loại": "truyện ngắn kinh dị", "sample": "Tối qua, con gái tôi dự tiệc sinh nhật và về nhà muộn. Sau khi cho con bé đi ngủ, tôi ngủ quên trên ghế phòng khách. Trong cơn mơ màng, tôi cảm thấy con bé kéo tay áo, thì thầm gọi: Bố ơi. Khi tôi tỉnh dậy, nó hỏi: Bố đoán xem tháng sau con mấy tuổi? Tôi còn chưa kịp trả lời, con bé đã lôi ra 4 ngón tay người từ túi áo. Đã 8 tiếng trôi qua, và con bé vẫn không chịu nói những ngón tay đó từ đâu ra."}}
            </example_26>
            <example_27>
                user: "truyện cười câu đố viện tâm thần 1"
                answer: {{"thể loại": "truyện cười", "sample": "2 bệnh nhân tâm thần đi chơi ven bờ hồ xong có 1 người rớt xuống nước, người còn lại liều mình nhảy xuống cứu. Hôm sau, viện trưởng đến nói với người đã nhảy xuống cứu bạn anh ta: Chúng tôi có 2 tin, tin tốt là anh được xuất viện vì hành động cứu người tối qua còn tin xấu là bạn anh đã treo cổ chết. Người bệnh òa khóc: huhu, chết rồi sao, tôi thấy anh ta bị ướt nên mới treo lên cho mau khô mà sao chết rồi"}}
            </example_27>
            <example_28>
                user: "truyện cười câu đố viện tâm thần 2"
                answer: {{"thể loại": "truyện cười", "sample": "Tại một bệnh viện tâm thần, bác sĩ vẽ lên bức tường một cánh cửa và nói với các bệnh nhân nếu ai đi qua được sẽ được ra viện. Nhiều người thay nhau lao nhao đâm đầu vô tường và BS khoanh tay đắc thắng rồi chợt nhận ra có 1 bệnh nhân chắp tay sau đít cười khẩy. Vị BS thấy hài lòng vì có khả năng người này đã khỏi và đi lại hỏi: vì sao anh ko tham gia cùng họ, anh không muốn ra viện à. Bệnh nhân cười lớn trước sự trông chờ 1 câu trả lời từ BS, sau đó nói: BS biết tại sao tụi nó không vượt qua được k, tôi đang giữ chìa khóa mà"}}
            </example_28>
            <example_29>
                user: "truyện cười câu đố viện tâm thần 3"
                answer: {{"thể loại": "truyện cười", "sample": "Tại 1 bệnh viện, bác sĩ thấy một bệnh nhân tâm thần đang ngồi ngắm thiên nhiên. Ông ta liền hỏi: anh có biết tại sao con kiến có thể bay hay k? Bệnh nhân: nó có cánh. BS: Nó ko có cánh nhưng nó đã uống thuốc thần. Bệnh nhân có vẻ ko vừa ý và đáp: Vậy BS có biết vì sao con thằn lằn có thể bay hay k? BS: đơn giản thôi nó cũng uống viên thuốc đó. Bệnh nhân: Không, nó chỉ cần ăn con kiến kia thôi. Bệnh nhân lại tiếp: thế ông có biết vì sao con đại bàng có thể bay k? BS cay cú đáp liền: nó cũng uống thuốc chứ gì? Bệnh nhân đắc chí phá lên: con đại bàng nào chả bay được, thằng bị tâm thần là ông mới đúng"}}
            </example_29>
            <example_30>
                user: "Bus to school"
                answer: {{"thể loại": "truyện ngắn kinh dị", "sample": "Như thường lệ, tôi ngồi trên xe buýt đến trường, chỉ lơ đãng nhìn quanh. Tại điểm dừng nhà Tommy, một bàn tay lướt qua cửa sổ xe bus, vẫy tay ra hiệu cho tài xế đi tiếp. Tôi nghĩ chắc cậu ấy ốm. Hôm sau, xe bus lại dừng trước nhà Tommy. Khi định báo tài xế chuyện đã xảy ra, tôi thấy cảnh tượng ám ảnh: một bàn tay nhợt nhạt lại lướt qua cửa sổ, vẫy tay ra hiệu đi tiếp, y hệt hôm trước. Tôi biết vì tối qua tôi đã đọc bản tin ả nhà Tommy bị sát hại chiều qua"}}
            </example_30>
            <example_31>
                user: "cà khịa tô lâm và nghị định 168 cái đéo gì cũng phạt"
                answer: {{"thể loại": "truyện cười", "sample": "Một ngày nọ, đồng chí Lú khuất núi và chó Tô lên thay. Chó Tô và đồng bọn trước giờ bị chèn ép và chửi bới nên từ ngày chó Tô được bầu làm chủ tịch Hắc Cẩu Bang và lũ chó lông vàng bắt đầu lộng hành. Chúng đi khắp nơi, sủa càn cắn bậy, vơ vét của cải khắp nơi, già không bỏ, nhỏ không tha với điều luật 168. Trong Hán cẩu tự, 168 là một lần mãi phát lộc; âm mưu chèn ép và hủy diệt cư dân làng Đổn đã có từ nay. Tuy nhiên, lưới trời lồng lộng, một ngày nọ Hắc cẩu hội trong một chuyến du hí ăn thịt bò dát vàng đã bị phiến quân Gấu xám xứ bạch dương ám sát, kết thúc một đời Ô NHỤC của ĐĨ CHÓ HỌ TÔ"}}
            </example_31>
    """
    
    return samples