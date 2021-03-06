vals = """BEST_PICTURE = [The Big Short, Bridge of Spies, Brooklyn, Mad Max: Fury Road, The Martian, The Revenant, Room, Spotlight]

BEST_ACTOR = [Bryan Cranston Trumbo, Matt Damon The Martian, Leonardo DiCaprio The Revenant, Michael Fassbender Steve Jobs, Eddie Redmayne The Danish Girl]

BEST_ACTRESS = [Cate Blanchett Carol, Brie Larson Room, Jennifer Lawrence Joy, Charlotte Rampling 45 Years, Saoirse Ronan Brooklyn]

BEST_SUPPORTING_ACTOR = [Christian Bale The Big Short, Tom Hardy The Revenant, Mark Ruffalo Spotlight, Mark Rylance Bridge of Spies, Sylvester Stallone Creed]

BEST_SUPPORTING_ACTRESS = [Jennifer Jason Leigh The Hateful Eight, Rooney Mara Carol, Rachel McAdams Spotlight, Alicia Vikander The Danish Girl, Kate Winslet Steve Jobs]

DIRECTING = [Adam McKay The Big Short, George Miller Mad Max Fury Road, Alejandro G. Inarritu The Revenant, Lenny Abrahamson Room, Tom McCarthy Spotlight]

ANIMATED_FEATURE_FILM = [Anomalisa, Boy and the World, Inside Out, Shaun the Sheep Movie, When Marnie Was There]

COSTUME_DESIGN = [Carol, Cinderella, The Danish Girl, Mad Max Fury Road, The Revenant]

DOCUMENTARY_FEATURE = [Amy, Cartel Land, The Look of Silence, What Happened Miss Simone, Winter on Fire]

DOCUMENTARY_SHORT = [Body Team, Chau Beyond the Lines, Claude Lanzmann, A Girl in the River The Price of Forgiveness, Last Day of Freedom]

MAKEUP_AND_HAIR_STYLING = [Mad Max Fury Road, The Hundred-Year-Old Man Who Climbed Out the Window and Disappeared, The Revenant]

ORIGINAL_SONG = [Earned It Fifty Shades of Grey, Manta Ray Racing Extinction, Simple Song #3 Youth, Til It Happens to You The Hunting Ground, Writing's on the Wall Spectre]

ANIMATED_SHORT = [Bear Story, Prologue, Sanjay's Super Team, We Can't Live Without Cosmos, World of Tomorrow]

SOUND_EDITING = [Mad Max Fury Road, Sicario, Star Wars The Force Awakens, The Martian, The Revenant]

FILM_EDITING = [The Big Short, Mad Max Fury Road, The Revenant, Spotlight, Star Wars The Force Awakens]

FOREIGN_LANGUAGE_FILM = [Embrace of the Serpent, Mustang, Son of Saul, Theeb, A War]

ORIGINAL_SCORE = [Bridge of Spies, Carol, The Hateful Eight, Sicario, Star Wars The Force Awakens]

PRODUCTION_DESIGN = [Bridge of Spies, The Danish Girl, Mad Max Fury Road, The Martian, The Revenant]

VISUAL_EFFECTS = [Ex Machina, Mad Max Fury Road, The Martian, The Revenant, Star Wars The Force Awakens]

ADAPTED_SCREENPLAY = [The Big Short, Brooklyn, Carol, The Martian, Room]

ORIGINAL_SCREENPLAY = [Bridge of Spies, Ex Machina, Inside Out, Spotlight, Straight Outta Compton]

BEST_CINEMATOGRAPHY = [Carol, The Hateful Eight, Mad Max Fury Road, The Revenant, Sicario]"""

for i, c in enumerate(vals):
    if c == '[' or (c == ' ' and vals[i-1] == ','):
        vals = vals[i:] + """'""" + vals[:i]
    elif c in [']', ',']:
        vals = vals[i-1:] + """'""" + vals[:i-1]
print vals
