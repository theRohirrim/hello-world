import random

who = ["A rabbit", "A hobo", "My mother", "The state governor of Montana",
       "My long lost pet sea turtle", "Istanbuls most famous rock merchant", "Yeovils local clown",
       "your dads cousin", "My cousins dad who forces everyone to call him by his chosen nickname",
       "My aquaintence whomstdve I want to stab every now and then",
       "This lady who berates me for simple mistakes",
       "Some bozo who cant even type"
       "The night worker who works on Fiddle Street corner"]
when = ["last night", "when my glutes started expanding",
        "around the time you told me your dad started peeing the colour magenta",
        "before the trees grew tall and roots deep", "when the world was still full of magic",
        "probably around lunchtime tomorrow", "many moons ago", "this tuesday",
        "right before I entered my coma", 
        "right before my boyfriend laughed at his own toilet",
        "after the big event with nans explosive attacks",
        "just 30 seconds ago",
        "around the time when I lost my toes to a pack of wild dogs" ]
name = ["Charles", "Shezza",  "Bob", "Gary", "Bobkiss", "I think his name was El Pepito",
        "sounded similar to Karen Tankerton", "underwent a legal name change to Peter Pan Goku",
        "I think he goes by Dick Long", "Hitler Mussolini", "Mr. Muscle", "Fat Crap Bobby",
        "Teeny Weeny Peeny", "Spank Loveman", "Ruud Penis", "Flahglughlughlugh", "Crab-kits"]
what = ["commited murder", "tickled a turkey's gullet",  "stolen my twix",
        "rugby tackled a man in a wheelchair",
        "charged hitler with identity theft in the Argentinian municipality court of Valcheta",
        "commited LARSONY of DONALD TRUMPS hair",
        "started a fire with bodily hair collected from the local homeless population",
        "risked the structural integrity of a 12 storey residental complex with his fascination of explosives fashioned from kitchen appliances",
        "the wrote an the the eleven page the Yelp review the of the the the the the the nearest the Crazy the Frog impersonator, Michael Owen,",
        "entered a blood bond with a man some have claimed to be Princess Di's long lost eskimo lover",
        "refused to type fecal matters as court scribe when it came to a waste management judicial review",
        "lost an eye in his cereal",
        "lost some cereal in his eyes",
        "accused me of having a relationship with the town dog",
        "kicked enough stray cats to get the cops called",
        "asked me for the time but walked away before I could answer",
        "removed the packaging on all bags of fruit along the high street shops",
        "borrowed a bobbies police hat to take a selfie with a padestrians dog, subsequently nicknamed 'PC Poodle'"]
where = [", at Ohio State University",
         "in a sewer", "in a small town named 'Frome'",
         "under the YMCA bunk beds",
         "in Ted Bundy's basement",
         "at the cult leaders personal residence",
         "next to the place where I get my tacos",
         "on holiday in Germany next to your uncle's farm",
         "at Bob Barkers famous holiday retreat 'Succulent Bobs BASED Bachelor Pad'",
         "somewhere north of the M23",
         "at that hooker's place",
         "you know, that place next to where I murdered your dad in cold blood",
         "in that back alley. you remember, the one where your mate got his member caught in a discarded desk fan",
         "figuratively in my front garden", "in the local skate park"]
intro = ["Let me tell you a story, see.", "Listen up, buddy.", "Did you hear of this one?",
         "O Sorrow! O Woe! Lend me your ears to a tragic tale!",
         "This is a story all about how my life got turned right upside down.",
         "Before you walk away with my money and possessions, let me warn you with this.",
         "Alright so this one time...wait I forgot that one here is this one.",
         "Listen to this, right.", "Better listen to this as a cautionary tale."]
outro = [". Classic!",". Those were the days.", ". It was a better time.", ". Sometimes you just gotta go oldschool.",
         ", yet I still feel like it was only yesterday.", " but nothing has come close to being as interesting as that since.",
         " yet life goes on.", " so as you can imagine we haven't talked to them much since.", ". Funny stuff eh?"]

intro_line = random.choice(intro)
who_line = random.choice(who)
name_line = random.choice(name)
what_line = random.choice(what)
where_line = random.choice(where)
when_line = random.choice(when)
outro_line = random.choice(outro)

story = intro_line + " " + who_line + ", " + name_line + ", had one time " + what_line + " " + where_line + ". Oh this was " + when_line + outro_line

print(story)
