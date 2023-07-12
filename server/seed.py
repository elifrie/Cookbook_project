#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Local imports
from app import app
from models import db, Recipe, User, Category, Category_recipe

with app.app_context():
    db.drop_all()
    db.create_all()

    #List of categories
    category_data = [
        {"category": "Appetizers"},
        {"category": "Breads & Savory Pastries"},
        {"category": "Cakes & Sweet Pastries"},
        {"category": "Chicken"},
        {"category": "Cookies"},
        {"category": "Desserts (non pastries)"},
        {"category": "Drinks"},
        {"category": "Eggs"},
        {"category": "Fish & Seafood"},
        {"category": "Ground Meats"},
        {"category": "Hannukah"},
        {"category": "Jams, Marmalade, Granola, & more"},
        {"category": "Meat"},
        {"category": "Passover"},
        {"category": "Pasta"},
        {"category": "Potatoes"},
        {"category": "Rice"},
        {"category": "Rosh Hashanah"},
        {"category": "Sauces, Spreads, & Pastes"},
        {"category": "Soups"},
        {"category": "Sourdough Breads"},
        {"category": "Veggies & Salads"}
    ]

    def seed_categories():
        for data in category_data:
            category = Category(**data)
            db.session.add(category)

        db.session.commit()

    category_recipe_data = [
        {"category_id": 1, "recipe_id": 1}
    ]

    def seed_category_recipes():
        for data in category_recipe_data:
            category_recipe = Category_recipe(**data)
            db.session.add(category_recipe)
        
        db.session.commit()
    
    recipe_data = [
        {"user_id": "1", 
         
         "title": "Agedashi Tofu", 

         "picture": "", 

         "ingredients": """1 block medium-firm or firm tofu (1 pound) \n
         1 heaped tablespoon cornstarch\n
         1 heaped tablespoon tapioca starch\n
         1 heaped tablespoon flour\n
         ¼ teaspoon salt\n
         3-4 cups neutral-flavored oil for frying (vegetable, canola, etc)\n

         Sauce:\n
         1 cup dashi stock (use kombu dashi for vegetarian/vegan)\n
         2 Tbsp soy sauce\n
         2 Tbsp mirin\n
         Optional: 1 garlic clove halved\n
         Optional: ½ inch of ginger\n
         Optional: 2 inches kombu\n

         Toppings:\n
         1 daikon radish (1 daikon = 2.5 cm) (optional)\n
         2 green onion/scallion - green and light green parts only.\n
         ½ cup Katsuobushi (dried bonito flakes) (optional, and skip if vegetarian)\n
         Shichimi Togarashi (Japanese seven spice) (optional)\n""",

         "preparation": """Wrap the tofu with 3 layers of paper towels and place another plate on top. Drain the water out of tofu for 30-60 minutes.\n
         Mix the flour and the starches.\n
         Peel and grate the daikon and gently squeeze water out. Cut the green onion into thin slices. Dice the bonito flakes.\n
         Put all sauce ingredients - dashi, soy sauce, and mirin in a small saucepan and bring to a boil. Turn off the heat and set aside.\n
         Remove the tofu from paper towels and cut it into 6 blocks and then cut each block to 4. Total 24 pieces.\n
         Heat the oil to 350F (175C) in a deep fryer or medium saucepan. Work in two batches. Coat the tofu with flour mix, leaving excess flour, and immediately deep fry until they turn light brown and crispy. Turn if oil doesn’t cover, should take about 3-4 minutes.\n
         Remove the tofu and drain excess oil on the wire rack.\n
         5 minutes before serving, heat the oil to 375 f, move all the tofu to the pan in one layer, turning once and move to the wire rack. Should take 2-3 minutes.\n
         To serve, place the tofu in a serving bowl and gently pour the sauce without wetting the tofu. Garnish with grated daikon, green onion, katsuobushi, and shichimi togarashi.\n""", 
         "tips": "", 
         "reviews": ""
         },
        {"user_id": "1", 
         
         "title": "Baked feta with tomatoes and olives", 

         "picture": "", 

         "ingredients": """8 oz. block of feta\n
        2 cups cherry tomatoes, halved\n
        2 minced garlic cloves\n
        1 diced Fresno - mild hot pepper or sriracha\n
        1 diced red onion\n
        1 thinly sliced red pepper\n
        1 cup Kalamata olives, pitted and halved\n
        2-3 tablespoons chopped parsley\n
        10 chopped basil leaves\n
        1 tsp. chopped oregano (or ½ tsp. dried)\n
        ¼ tsp. black pepper, fresh cracked\n
        ½ teaspoon salt\n
        2 Tbsp. olive oil - divided.\n""",

         "preparation": """Preheat the oven to 400° F (205° C).\n
        Mix all ingredients other than feta with half the olive oil and place the rimmed oven safe baking dish or wide big pan.\n
        Bake for approximately 20 minutes until vegetables are roasted.\n
        Take out of the oven. Make room in the center and place the block of feta.  Sprinkle remaining 1 tablespoon of olive oil over the feta and veggies.\n
        Bake for approximately 15 minutes until vegetables are roasted and feta has softened.\n
        Serve with crackers and/or vegetable crudités.\n""", 
         "tips": "Serves 8", 
         "reviews": ""
         },
         {
            "user_id": 1,
            "title": "Chees Stuffed Mushrooms",
            "picture": "",
            "ingredients": """1½ pound fresh and very large (2 inches wide) mini bella mushrooms or championing mushrooms\n
            ⅔ pounds cheese blend - about 4 oz of each\n
            feta crumbs\n
            soft sheep cheese as chèvre\n
            Shredded hard sharp sheep cheese like cashcavale or moncello\n
            3-4 oz (80-100 gr) shredded mozzarella\n
            3-4 tablespoons pesto\n
            2 tablespoons pine nuts\n
            Salt as needed\n
            2 tablespoon olive oil\n""",

            "preparation": """Heat oven to 380 degrees\n
            Use a sharp paring knife carefully remove the mushroom stems completely to get the mushroom cups.\n
            Drizzle 1 tablespoon olive oil in a large Pyrex pan. Arrange the mushrooms in the pan.\n
            Put ½ teaspoon pesto in each mushroom.\n
            Drizzle remaining olive oil on top of mushrooms.\n
            If pesto is not salty enough drizzle some salt on the mushrooms.\n
            Place pine nuts on top of the pesto.\n
            Divide the cheese blend among the mushrooms and gently push into the cup.\n
            Drizzle mozzarella on top of cheese blend and gently tap so it sticks.\n
            Bake for about 25-30 minutes until mozzarella is brown\n""",

            "tips": "You can use less mozzarella and sprinkle gruyere on top. Then use a torch to melt it. ",
            "reviews": ""  
        } ,
        {
            "user_id": 1,
            "title": "Homemade Ricotta Cheese",
            "picture": "",

            "ingredients": """3 tablespoons balsamic white distilled vinegar\n
            1 tablespoons fresh lemon juice\n
            7 cups whole milk (not ultra-pasteurized)\n
            1 cup heavy cream (not ultra-pasteurized)\n
            2 tablespoons yogurt - preferably sheep\n
            Kosher salt - ½ teaspoon for sweet ricotta, 2 teaspoons for mild saltiness and 1 tablespoon for saltier ricotta.\n
            Serving suggestions: honey, cracked black pepper, fresh or dried fruit, fruit preserves, crackers or fresh bread\n""",
            
            "preparation": """Run a mosolin or a double layer of cheesecloth under warm water to dampen, then gently squeeze to remove any excess water. Line a colander with the cheesecloth and set in the sink.\n
            Bring the milk and cream to 190 degrees F, over medium-low heat, in a medium heavy-bottomed saucepan, stirring frequently to keep the milk mixture from scorching on the bottom. Don`t let it go over 195 degrees. Don’t stir with a whisker. Use a wooden or silicone spoon. Add yogurt, 1 tablespoon of the vinegar, and 1 the lemon, and salt and stir for 1 minutes on reduced heat (you'll see the milk mixture begin to slightly curdle). Remove from the heat, cover the saucepan with a lid and let sit for 20 minutes.\n
            Remove the lid and you'll see that the milk mixture has separated into small curds. Now stir in the remaining vinegar mixture and the milk mixture will continue to curdle. Stir for a few minutes. Pour this entire mixture into the prepared colander in the sink.\n
            Let drain until the desired texture, about 15 minutes for soft ricotta, 20 minutes for firm and creamy and 30 minutes for firm and slightly dry. If using a cheese basket, transfer the ricotta into it after 5 minutes and press gently to shape it.\n
            For soft ricotta, serve warm or chilled in a small decorative bowl. For firm ricottas, gather the excess cheesecloth and shape the ricotta into a ball or disc and refrigerate until chilled, at least 1 hour.\n
            You can eat or refrigerate up to 5 days.\n
            Serve the ricotta with your favorite things, like a drizzle of honey and cracked black pepper, fresh or dried fruit, fruit preserves, crackers or fresh bread.\n""",
            "tips": "",
            "reviews": ""
        },
        {
            "user_id": 1,

            "title": "Roasted Feta with Honey",

            "picture": "",

            "ingredients": """8-ounce slab Greek feta, blotted dry\n
            2 tablespoons extra-virgin olive oil\n
            1 tablespoon honey\n
            Freshly ground black pepper\n
            Fresh bread or pita bread cut into wedges\n
            (toasted if you like it better)\n
            Optional - a few sprigs of thyme, other herbs, or za'atar\n
            Optional for serving alongside - nuts, figs, tomatoes, etc. see below.\n""",

            "preparation": """Preheat the oven to 400 degrees. Select a small oven-to-table dish or a small ovenproof sauté pan. If you need to transfer the cheese to another plate after roasting, line it with parchment paper.\n
            Place the feta in the dish and cover with the olive oil. Bake until the cheese is soft and springy to the touch but not melted, about 8 minutes.\n
            Preheat the broiler or prepare your torch.\n
            Heat the honey in the microwave or over a pan of simmering water until it is fluid enough to be spread with a pastry brush and then paint the surface of the feta with it.\n
            Optional - throw a few scattered/sprigs of thyme or other fresh herbs or sprinkling za'atar on top.\n
            Broil or torch until the top of the cheese browns and just starts to bubble and brown. About 3 - 4 minutes. Watch carefully.\n
            Season to taste with black pepper.\n
            Serve immediately with bread or pita wedges\n
            Additional alongside serving suggestions -\n
            sliced heirloom tomatoes, cucumbers sprinkled with salt, pepper, or za’atar\n
            roasted cherry tomatoes in olive oil, salt, and pepper and served them alongside.\n
            roasted beets\n
            Roasted nuts on the side or on top.\n
            Fresh figs or quartered peaches and split figs under the broiler with the cheese, drizzled with honey.\n
            pickled vegetables\n""",

            "tips": "A drizzle of honey and a blast of heat transform a standard block of crumbly feta into an unexpectedly luscious, creamy spread for pita or a hunk of crusty bread. Perfect with a glass of red wine or chilled white wine.",

            "reviews": ""
        },
        {
            "user_id": 1,

            "title": "Tinned Tuna Fishcakes",

            "picture": "",

            "ingredients": """For the fish cakes\n
            1 medium potato (about 180g)\n
            1 small onion or 2 shallots (about 100g)\n
            1-2 carrot (about 140g), peeled and grated\n
            1 x 160g tin of tuna in oil, drained\n
            1 tbsp small baby capers or chopped larger ones, or even diced cucumber pickles\n
            ½-1 tbsp harissa paste, or a little more if you like some heat\n
            1 tbsp Dijon mustard\n
            2 tsp wholegrain mustard\n
            1 small bunch of parsley, chopped. Some can be replaced with cilantro, basil and mint.\n
            ½ tsp salt\n
            Optional: ½ tsp dashi powder\n
            Optional: lemon zest from half a lemon\n
            For frying\n
            2 medium egg\n
            70g flour\n
            1 tablespoon cornstarch\n
            1½ tsp smoked paprika\n
            ½ teaspoon salt\n
            Vegetable oil\n""",

            "preparation": """Place the potato and onion (both whole and unpeeled) in a small pan and cover with plenty of water and a teaspoon of salt. Boil until just soft - it should take about 20 to 25 minutes. Don`t be tempted to dice the potato before boiling, as it will retain too much water.\n
            Drain the pan and, once you can handle them easily, peel the potato and onion, and cut into small dice. Mix the diced vegetables with all the other ingredients for the fish cakes and make sure they are combined well.\n
            Create small rounded cakes - each about 50g. If they are very soft, place them in the fridge for 20 minutes; if they are nice and firm, you can cook them straight away.\n
            Lightly beat the egg in a small bowl. Mix the flour, cornstarch, paprika, and salt together in a separate bowl.\n
            Heat a good amount of oil - about 2cm deep - in a frying pan to around 170C. Prepare a plate with some kitchen paper on it.\n
            Toss each cake in the seasoned flour and then dip it into the egg. Carefully pop into the hot oil. Fry until beautifully golden on the bottom, then flip and fry the other side (it should take about two minutes each side).\n
            If your oil is getting too hot, remove it from the hob for a few seconds and reduce the heat.\n
            Serve hot, or at room temperature, or in pitta bread, along with some yogurt, maybe some sliced vegetables, and a squeeze of lemon.\n""",

            "tips": "Use yellow or gold potatoes which are starchy. It will bring the cakes together. ",

            "reviews": ""
        },
        {
            "user_id": 1,

            "title": "Test",

            "picture": "",

            "ingredients": "sdfa",

            "preparation": "dsdf",

            "tips": "adsfasdf",

            "reviews": "adsfa"
        },
    ]

    def seed_recipes():
        for data in recipe_data:
            recipe = Recipe(**data)
            db.session.add(recipe)

        db.session.commit()

    user_data = [
        {"username": "Chuchu", "password": "mayolover"}
    ]

    def seed_users():
        for data in user_data:
            user = User(**data)
            db.session.add(user)
        
        db.session.commit()
    
    def seed():
        seed_categories()
        seed_category_recipes()
        seed_recipes()
        seed_users()
    
    seed()
    print('Categories, category_recipes, recipes, and users Seeded!')

    