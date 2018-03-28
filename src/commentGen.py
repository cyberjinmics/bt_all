#!/usr/bin/env python
# -*- coding: utf-8 -*-


from random import *
import random
import itertools

min_tags = 3
emojis = [u'🚀', u'😍', u'🌅', u'🎆', u'🎁', u'🎇', u'🌈', u'😘', u'😋']
comment_list = [
    ["this", "the", "your"],
    ["photo", "picture", "pic", "shot", "snapshot"],
    ["is", "looks", "feels", "is really"],
    ["great", "super", "good", "very good", "good", "wow", "WOW", "cool", "GREAT", "magnificent", "magical", "very cool",
     "stylish", "beautiful", "so beautiful", "so stylish", "so professional", "lovely", "so lovely", "very lovely", "glorious",
     "so glorious", "very glorious", "adorable","excellent", "amazing"],
    [".", "..", "...", "!", "!!", "!!!"]
]
comments = [
    'Nice one', 'Love this one.', 'Hmm. What a post.', 'This one dey shackle shackle me.', 'Your is xoo nice.',
    'Please check your inbox.', 'Please follow my account.', 'I\'d like to know you better.', 'Works like charm.',
    'I\'m a living testimony of this.', 'How can I advertise on your account?', 'Can you help me advertise on your account?',
    'Can I sponsor your posts?', 'Can we be friends please?', 'This on the pick. Nice one.', 'Great!', 'Nice.', 'Good',
    'Xo Jolly', 'The bloody goody post', 'What a sparkling post.', 'Just like this one.', 'I think this one is the best.',
    'What I think? Xo kuul.', 'Got me on the nerves.', 'Love is superb.', 'One more please.', 'What?!', 'Fuu.nke!',
    'Apostle will here of this.', 'Hmmm... Mind boogles.', 'More than nice.', 'Jez the type I searched for.', 'Please like my post.',
    'Just the best.', 'All is well', 'Oh my....', 'OoooKay.', 'We love this. Sorry. I love this.', 'Healing dose.',
    'Therapeutical', 'Keep it rolling in.', 'Got my eyes glued.', 'Mouth agape.', 'Smells like pizza.', 'Sings melody.',
    'Wow! This is nice.', 'Wanted to use a gif. Add gif instagram.', 'Must show this to my...', 'Mustn\'t see this alone.',
    'Can\'t be selfish on this. I should share.', 'Got to share this.', 'Got tag.', 'Perfect. In the voice of Ed Sheeran.',
    'Nice 1.', '9ice 1.', 'Oh yeah. Like power.', 'Took my breathe.', 'Away with silence. This is nice.',
    'How do I? Say it\'s not mind-blowing.', 'Professional shot there.', 'Looks like a finescape.', 'Jesus is comming soon.'
    u'End time sign😃', u'What the eyes have not seen😍', 0
]
instaAccount = 'shopbraid'
category = ''
comment = ''
def commentGen(tags_count, caption, mention):
    media_count = tags_count
    if tags_count < min_tags:
        tags_count = min_tags

    adjectives = [
    ]

    hashtags = [
        '#cars247', '#bugatti', '#f1', '#217mph', '#car', '#cars', '#supercar', '#supercars', '#auto', '#automotive',
        '#blacklist', '#bike', '#bikes', '#motorsports', '#carinstagram', '#россия', '#racing', '#amazing_cars', '#авто',
        '#москва', '#itswhitenoise', '#машина', '#amazingcars', '#carswithoutlimits', '#whipztagram', '#lambo',
        '#mydubai', '#dxb', '#sportscar', '#carlifestyle', '#carspotter', '#carslover', '#autoshow', '#carshow',
        '#carspushingthelimits', '#wheels', '#carsandcoffee', '#luxurycar', '#carspotting', '#amazingcars247', '#luxurycars',
        '#chiron', '#gorecon', '#recon', '#getlit', '#ford', '#dodge', '#chevy', '#gmc', '#toyota', '#lit', '#led', '#lighting',
        '#lifted', '#liftedtruck', '#truck', '#trucks', '#showtruck', '#diesel', '#diesellovers', '#rollingcoal', '#offroad',
        '#gamechanger', '#featuredfollower', '#tagafriend', '#followus', '#trucklights', '#truckporn', '#trucklife', '#milano',
        '#alpi', '#dolomiti', '#acmilan', '#fcinter', '#inquinamento', '#toyotahybrid', '#toyotanation', '#sefcarmilano', '#design',
        '#4x4', '#brera', '#portanuova', '#navigli', '#toyotadakar', '#toyotahilux', '#newhilux', '#hilux', '#carstagram', '#motor',
        '#yellowcar', '#mercedesf1', '#mercedesbenz', '#mercedesamg', '#mercedes', '#amg', '#benz', '#brabus', '#favorite',
        '#luxuryrate', '#moscow', '#mafia', '#fenyr', '#supersport', '#wmotors', '#kacafilmmobil', '#kacafilm', '#modifikasi',
        '#3mwindowfilm', '#3m', '#peddlersvillage', '#challengerlifts', '#mechanic', '#sitevisit', '#proauto', '#workshop',
        '#softskills', '#training', '#student', '#safetydriving', '#kuching', '#trainer', '#gtc', '#roadster', '#v8', '#biturbo',
        '#photo', '#fastcar', '#engine', '#horsepower', '#autogespot', '#money', '#dubai', '#beast', '#nikontop', '#photography',
        '#photooftheday', '#post', '#monaco', '#follow', '#basel', '#switzerland', '#guimaraes', '#clientefeliz', '#autospot',
        '#blackfriday', '#jeeplovers', '#jeep', '#grandcherokee', '#cherokee', '#luxury', '#sport', '#sportcars', '#instafollow',
        '#instacar', '#instaauto', '#caroftheday', '#autocar', '#picture', '#motors', '#motorsport', '#followers', '#instagram',
        '#vehicles', '#autos', '#compra', '#buy', '#sale', '#dealer', '#exoticcar', '#porsche', '#918spyder', '#cargram', '#instacars',
        '#hypercars', '#hybrid', '#carphotography', '#automotivephotography', '#carheaven', '#stuttgard', '#porschepix', '#porsches',
        '#race', '#dreamcar', '#benzliving', '#kingzwhips', '#holiday', '#maulidnabi', '#islam', '#maxprowindowfilms', '#madeinusa',
        '#windowfilm', '#windowtint', '#kacafilmgedung', '#jualkacafilm', '#pasangkacafilm', '#modifikasimobil', '#aksesorismobil',
        '#banmobil', '#velgmobil', '#sarungjok', '#lippocikarang', '#lippogroup', '#meikarta', '#muscle', '#musclecar', '#drive',
        '#ride', '#speed', '#street', '#m3', '#e46', '#bmwm', '#mpower', '#sti', '#bmw', '#lamborghini', '#ferrari', '#exoticcars',
        '#jdm', '#f4f', '#beastmode', '#picoftheday', '#wrx', '#hypebeast', '#tb', '#ledworklight', '#worklight', '#offroadled',
        '#ledlightbar', '#foglights', '#foglight', '#ledheadlamp', '#jeepcap', '#autoparts', '#faros', '#farosled', '#lightbar',
        '#headlamps', '#offroadlights', '#barrasled', '#suzuki', '#jeepwrangler', '#offroadlightbar', '#jeepparts', '#ledlights',
        '#performanceaudi', '#racinglineperformance', '#racingline', '#rline', '#audiuk', '#audi', '#b9', '#s4', '#audis4',
        '#audizine', '#campallroad', '#audigramm', '#night', '#lightpainting'
    ]

    if caption == 'hashtags':
        comment = " ".join(sample(hashtags, tags_count))
    elif caption == 'caption':
        comment = mention + ' '
        comment = comment + random.choice(emojis)
    elif caption == 'post_comment':
        comment = random.choice(comments)
        if comment == 0:
            c_list = list(itertools.product(*comment_list))
            repl = [("  ", " "), (" .", "."), (" !", "!")]
            res = " ".join(random.choice(c_list))
            for s, r in repl:
                res = res.replace(s, r)
            comment = res.capitalize()
    return comment
