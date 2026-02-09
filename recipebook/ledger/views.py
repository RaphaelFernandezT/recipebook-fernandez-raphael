from django.shortcuts import render

def homepage(request):
    return render(request, "ledger/homepage.html")

def recipelist(request):
    ctx1 = {
        "recipes": [
            {
                "name": "Recipe 1",
                "ingredients": [
                    {
                        "name": "tomato",
                        "quantity": "3pcs"
                    },
                    {
                        "name": "onion",
                        "quantity": "1pc"
                    },
                    {
                        "name": "pork",
                        "quantity": "1kg"
                    },
                    {
                        "name": "water",
                        "quantity": "1L"
                    },
                    {
                        "name": "sinigang mix",
                        "quantity": "1 packet"
                    }
                ],
                "link": "ledger/recipe/1"
            },
            {
                "name": "Recipe 2",
                "ingredients": [
                    {
                        "name": "garlic",
                        "quantity": "1 head"
                    },
                    {
                        "name": "onion",
                        "quantity": "1pc"
                    },
                    {
                        "name": "vinegar",
                        "quantity": "1/2cup"
                    },
                    {
                        "name": "water",
                        "quantity": "1 cup"  # Fixed typo: "quanity" → "quantity"
                    },
                    {
                        "name": "salt",
                        "quantity": "1 tablespoon"
                    },
                    {
                        "name": "whole black peppers",
                        "quantity": "1 tablespoon"
                    },
                    {
                        "name": "pork",
                        "quantity": "1 kilo"
                    }
                ],
                "link": "ledger/recipe/2"
            }
        ]
    }    
    return render(request, "ledger/recipelist.html", ctx1)

def recipe1(request):
    ctx2 = {
        "name": "Recipe 1",
        "ingredients": [
            {
                "name": "tomato",
                "quantity": "3pcs"
            },
            {
                "name": "onion",
                "quantity": "1pc"
            },
            {
                "name": "pork",
                "quantity": "1kg"
            },
            {
                "name": "water",
                "quantity": "1L"
            },
            {
                "name": "sinigang mix",
                "quantity": "1 packet"
            }
        ],
        "link": "ledger/recipe/list"
    }
    return render(request, "ledger/recipe1.html", ctx2)

def recipe2(request):
    ctx3 = {
            "name": "Recipe 2",
            "ingredients": [
                {
                    "name": "garlic",
                    "quantity": "1 head"
                },
                {
                    "name": "onion",
                    "quantity": "1pc"
                },
                {
                    "name": "vinegar",
                    "quantity": "1/2cup"
                },
                {
                    "name": "water",
                    "quantity": "1 cup"
                },
                {
                    "name": "salt",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "whole black peppers",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "pork",
                    "quantity": "1 kilo"
                }
            ],
            "link": "/recipe/2"
        }
    return render(request, "ledger/recipe1.html", ctx3)