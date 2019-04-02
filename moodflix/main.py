import webapp2
import jinja2
import os
from models import Movie
from google.appengine.ext import ndb
from google.appengine.api import urlfetch
import json
import urllib



the_jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = [],
    autoescape = True)

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_environment.get_template('templates/welcome.html')
        self.response.write(welcome_template.render())
        print("welcomeget")

    def post(self):
        print("WelcomePost")
        mood = self.request.get('mood')
        occasion = self.request.get('occasion')
        result_template = the_jinja_environment.get_template('templates/loading.html')
        self.response.write(welcome_template.render())



# class Upload(webapp2.RequestHandler):  # todo: not adding movies
#     def get(self):
#         welcome_template = the_jinja_environment.get_template('templates/loading.html')
#         mood = self.request.get('mood')
#         occasion = self.request.get('occasion')
#         print("uploadget")
#         print(mood)
#         print(occasion)
#         shrek = Movie(title='Shrek', duration=123, rating=10, description='About an ogre who lives in a swamp.', mood='humorous', occasion='family night')
#         shrek_key = shrek.put()
#         thor = Movie(title='Thor: Ragnarok', duration=130, rating=8, description='Thor is imprisoned on the planet Sakaar, and must race against time to return to Asgard and stop Ragnarok, the destruction of his world, at the hands of the powerful and ruthless villain Hela.', mood='humorous, cheerful', occasion='casual watching')
#         thor_key = thor.put()
#         wake = Movie(title='Before I wake', duration=97, rating=6, description='A couple adopt an orphaned child whose dreams - and nightmares - manifest physically as he sleeps.', mood='gloomy', occasion='halloween based')
#         wake_key = wake.put()
#         santa = Movie(title='Santa Buddies', duration=88, rating=5, description='At the North Pole, Santa Claus (Father Christmas) and his chief dog Santa Paws worry as the whole toy processing system is threatened by the weakening of its magical power source, the icicle drawing on Christmas spirit.', mood='cheerful', occasion='Christmas')
#         pounds = Movie(title='Seven Pounds', duration=123, rating=8, description='A man with a fateful secret embarks on an extraordinary journey of redemption by forever changing the lives of seven strangers.', mood='inspirational', occasion='casual watching')
#         self.response.write(welcome_template.render())
#
#     def post(self):
#         mood = self.request.get('mood')
#         occasion = self.request.get('occasion')
#         result_template = the_jinja_environment.get_template('templates/result.html')
#         self.response.write(result_template.render())

class ResultPage(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_environment.get_template('templates/result.html')
        mood = self.request.get("mood")
        occasion = self.request.get("occasion")
        # print("Resultget")
        # print(mood)
        # print(occasion)
        movie_query = Movie.query()
        all_movies = movie_query.fetch()
        rec_movies = []
        for movie in all_movies:
            if (movie.mood in mood) and (movie.occasion in occasion):
                rec_movies.append(movie)
        movie_dic = {
            "movies": rec_movies
        }
        self.response.write(welcome_template.render(movie_dic))


    def post(self):
        mood = self.request.get("mood")
        occasion = self.request.get("occasion")
        if Movie.query().count() == 0:
            shrek = Movie(title='Shrek', duration=123, rating=10, description='About an ogre who lives in a swamp.', mood='humorous, gloomy', occasion='family night, playdate')
            shrek_key = shrek.put()
            print("adding movies")
            thor = Movie(title='Thor: Ragnarok', duration=130, rating=8, description='Thor is imprisoned on the planet Sakaar, and must race against time to return to Asgard and stop Ragnarok, the destruction of his world, at the hands of the powerful and ruthless villain Hela.', mood='humorous, cheerful, gloomy', occasion='casual watching, alone time')
            thor_key = thor.put()
            wake = Movie(title='Before I wake', duration=97, rating=6, description='A couple adopt an orphaned child whose dreams - and nightmares - manifest physically as he sleeps.', mood='gloomy', occasion='halloween')
            wake_key = wake.put()
            santa = Movie(title='Santa Buddies', duration=88, rating=5, description='At the North Pole, Santa Claus (Father Christmas) and his chief dog Santa Paws worry as the whole toy processing system is threatened by the weakening of its magical power source, the icicle drawing on Christmas spirit.', mood='cheerful', occasion='christmas')
            santa_key = santa.put()
            pounds = Movie(title='Seven Pounds', duration=123, rating=8, description='A man with a fateful secret embarks on an extraordinary journey of redemption by forever changing the lives of seven strangers.', mood='inspirational', occasion='casual watching, indecisive, alone time')
            pounds_key = pounds.put()
            moana = Movie(title='Moana', duration=107, rating=8, description="In Ancient Polynesia, when a terrible curse incurred by the Demigod Maui reaches Moana's island, she answers the Ocean's call to seek out the Demigod to set things right.", mood='cheerful, mellow, gloomy, energetic', occasion='family night, playdate, casual watching')
            moana_key = moana.put()
            despicable = Movie(title='Despicable Me 3', duration=89, rating=6, description='Gru meets his long-lost charming, cheerful, and more successful twin brother Dru who wants to team up with him for one last criminal heist.', mood='humorous, cheerful', occasion='playdate, family night')
            despicable_key = despicable.put()
            cars = Movie(title='Cars 3', duration=102, rating=7, description="Lightning McQueen sets out to prove to a new generation of racers that he's still the best race car in the world.", mood='cheerful, energetic', occasion='casual watching, alone time')
            cars_key = cars.put()
            sing = Movie(title='Sing',duration=108, rating=7, description="In a city of humanoid animals, a hustling theater impresario's attempt to save his theater with a singing competition becomes grander than he anticipates even as its finalists' find that their lives will never be the same.", mood='energetic, cheerful, melancholy', occasion='family night, playdate')
            racer = Movie(title='Speed Racer', duration=135, rating=6, description='A young driver, Speed Racer, aspires to be champion of the racing world with the help of his family and his high-tech Mach 5 automobile.', mood='energetic, melancholy', occasion='family night, alone time, casual watching')
            racer_key = racer.put()
            jedi = Movie(title='Star Wars: The Last Jedi', duration=152, rating=7, description='Rey develops her newly discovered abilities with the guidance of Luke Skywalker, who is unsettled by the strength of her powers. Meanwhile, the Resistance prepares for battle with the First Order.', mood='energetic, cheerful', occasion='indecisive, casual watching')
            jedi_key = jedi.put()
            hercules = Movie(title='Hercules', duration=93, rating=7, description='The son of the Greek Gods Zeus and Hera is stripped of his immortality as an infant and must become a true hero in order to reclaim it.', mood='nostalgic, cheerful, melancholy', occasion='casual watching, indecisive, playdate')
            hercules_key = hercules.put()
            bourne = Movie(title='The Bourne Ultimatum', duration=115, rating=8, description='Jason Bourne dodges a ruthless CIA official and his agents from a new assassination program while searching for the origins of his life as a trained killer.', mood='energetic', occasion='alone time, casual watching, indecisive')
            bourne_key = bourne.put()
            playdate = Movie(title='Playdate', duration=82, rating=5, description='After befriending a family that has just moved in next door, Emily Valentine begins to realize that these new neighbors are hiding a deadly secret.', mood='gloomy', occasion='indecisive, halloween')
            playdate_key = playdate.put()
            house = Movie(title='The House Next Door', duration=137, rating=7, description='A happy couple faces horror when a family moves into the neighborhood.', mood='gloomy', occasion='halloween, indecisive')
            house_key = house.put()
            childhood = Movie(title='The Childhood of a Leader', duration=115, rating=6, description='A chronicle of the childhood of a post-World War I leader.', mood='gloomy', occasion='halloween, casual watching')
            childhood_key = childhood.put()
            boy = Movie(title='The Boy', duration=97, rating=6, description="An American nanny is shocked that her new English family's boy is actually a life-sized doll. After she violates a list of strict rules, disturbing events make her believe that the doll is really alive.", mood='gloomy', occasion='halloween, casual watching')
            boy_key = boy.put()
            grinch = Movie(title='How the Grinch stole Christmas', duration=104, rating=6, description='On the outskirts of Whoville, there lives a green, revenge-seeking Grinch who plans on ruining the Christmas holiday for all of the citizens of the town.', mood='cheerful, mellow, melancholy', occasion='christmas, indecisive, casual watching')
            grinch_key = grinch.put()
            mickey = Movie(title="Mickey's Magical Christmas: Snowed in at the House of Mouse", duration=61, rating=7, description="Mickey and all his friends hold their own Christmas party at the House of Mouse, after being snowed in.", mood='nostalgic, cheerful, melancholy', occasion='christmas, family night, casual watching')
            mickey_key = mickey.put()
            dear = Movie(title='Dear Santa', duration=90, rating=7, description='A young woman who comes from a life of privilege falls for the owner of a soup kitchen after discovering a Dear Santa letter written by his seven year old daughter.', mood='inspirational, mellow', occasion='christmas, indecisive')
            dear_key = dear.put()
            project = Movie(title='The Christmas Project', duration=92, rating=6, description='A writer looks back on his memorable 1986 Christmas, dealing with brothers, bullies, first love, pregnancy and family "elving."', mood='inspirational, cheerful, melancholy', occasion='christmas, family night, casual watching')
            project_key = project.put()
            coffee = Movie(title='Coffee Shop', duration=88, rating=6, description='When a young coffee shop owner is threatened with repossession she must take a chance with life and love as she fights to save her business.', mood='romantic, mellow', occasion='date night, alone time, christmas')
            coffee_key = coffee.put()
            mamma = Movie(title='Mamma Mia', duration=108, rating=7, description='The story of a bride-to-be trying to find her real father told using hit songs by the popular 1970s group ABBA.', mood='romantic, humorous', occasion='date night, indecisive')
            mamma_key = mamma.put()
            souls = Movie(title='Our Souls at Night', duration=103, rating=7, description="Fonda and Redford will star as Addie Moore and Louis Waters, a widow and widower who've lived next to each other for years. The pair have almost no relationship, but that all changes when Addie tries to make a connection with her neighbor.", mood='romantic, mellow', occasion='date night, casual watching')
            souls_key = souls.put()
            before = Movie(title='Before We Go', duration=95, rating=7, description="Two strangers stuck in Manhattan for the night grow into each other's most trusted confidants when an evening of unexpected adventure forces them to confront their fears and take control of their lives.", mood='romantic, cheerful', occasion='date night')
            before_key = before.put()
            set = Movie(title='Set It Up', duration=105, rating=7, description='Two corporate executive assistants hatch a plan to match-make their two bosses.', mood='humorous, romantic, melancholy', occasion='date night, casual watching, indecisive')
            set_key = set.put()
            mile = Movie(title='1 Mile to You', duration=104, rating=6, description="After a teenager's friends die in an accident, he finds running allows him to remember them perfectly. Running, however, also brings him notoriety. He is caught between keeping the past alive and making new memories in the present.", mood='inspirational', occasion='casual watching, indecisive')
            mile_key = mile.put()
            katwe = Movie(title='Queen of Katwe', duration=124, rating=6, description='A Ugandan girl sees her world rapidly change after being introduced to the game of chess.', mood='inspirational, cheerful', occasion='casual watching, indecisive, alone time')
            katwe_key = katwe.put()
            fourty = Movie(title='42',duration=128, rating=8, description='In 1947, Jackie Robinson becomes the first African-American to play in Major League Baseball in the modern era when he was signed by the Brooklyn Dodgers and faces considerable racism in the process.', mood='inspirational, cheerful', occasion='casual watching, alone time, indecisive')
            fourty_key = fourty.put()
            lion = Movie(title='Lion', duration=118, rating=8, description='A five-year-old Indian boy gets lost on the streets of Calcutta, thousands of kilometers from home. He survives many challenges before being adopted by a couple in Australia. 25 years later, he sets out to find his lost family.', mood='inspirational, mellow', occasion='casual watching, alone time, indecisive')
            lion_key = lion.put()
            paddington = Movie(title='Paddington', duration=95, rating=7, description='A young Peruvian bear travels to London in search of a home. Finding himself lost and alone at Paddington Station, he meets the kindly Brown family, who offer him a temporary haven.', mood='humorous, cheerful', occasion='family night, casual watching, indecisive, playdate')
            paddington_key = paddington.put()
            trolls = Movie(title='Trolls', duration=92, rating=7, description='After the Bergens invade Troll Village, Poppy, the happiest Troll ever born, and the curmudgeonly Branch set off on a journey to rescue her friends.', mood='energetic, humorous', occasion='family night, casual watching, playdate')
            trolls_key = trolls.put()
            dory = Movie(title='Finding Dory', duration=97, rating=7, description='The friendly but forgetful blue tang fish, Dory, begins a search for her long-lost parents, and everyone learns a few things about the real meaning of family along the way.', mood='humorous, cheerful', occasion='family night, casual watching, playdate')
            dory_key = dory.put()
            monsters = Movie(title='Monsters vs Aliens', duration=94, rating=7, description='A woman transformed into a giant after she is struck by a meteorite on her wedding day becomes part of a team of monsters sent in by the U.S. government to defeat an alien mastermind trying to take over Earth.', mood='humorous, energetic, cheerful', occasion='family night, casual watching, alone time, playdate')
            monsters_key = monsters.put()
            hotels = Movie(title='Hotel for Dogs', duration=100, rating=6, description='Two kids secretly take in stray dogs at a vacant hotel.', mood='humorous, cheerful', occasion='family night, alone time, casual watching')
            hotels_key = hotels.put()
            coco = Movie(title='Coco', duration=105, rating=8, description="Aspiring musician Miguel, confronted with his family's ancestral ban on music, enters the Land of the Dead to find his great-great-grandfather, a legendary singer.", mood='mellow, cheerful', occasion='casual watching, indecisive, family night')
            coco_key = coco.put()
            jurassic = Movie(title='Jurassic Park', duration=127, rating=8, description='During a preview tour, a theme park suffers a major power breakdown that allows its cloned dinosaur exhibits to run amok.', mood='nostalgic, mellow', occasion='casual watching, indecisive, alone time')
            jurassic_key = jurassic.put()
            coraline = Movie(title='Coraline', duration=100, rating=8, description='An adventurous 11-year-old girl finds another world that is a strangely idealized version of her frustrating home, but it has sinister secrets.', mood='gloomy', occasion='halloween, casual watching, alone time')
            coraline_key = coraline.put()
            kubo = Movie(title='Kubo and the Two Strings', duration=101, rating=8, description='A young boy named Kubo must locate a magical suit of armour worn by his late father in order to defeat a vengeful spirit from the past.', mood='cheerful', occasion='casual watching, indecisive, playdate')
            kubo_key = kubo.put()
            tangerine = Movie(title='Tangerine', duration=108, rating=7, description='A hooker tears through Tinseltown on Christmas Eve searching for the pimp who broke her heart.', mood='humorous, cheerful', occasion='casual watching, alone time, indecisive')
            tangerine_key = tangerine.put()
            gilmore = Movie(title='Happy Gilmore', duration=92, rating=7, description="A rejected hockey player puts his skills to the golf course to save his grandmother's house.", mood ='humorous, cheerful', occasion='alone time, casual watching')
            gilmore_key = gilmore.put()
            thirteen = Movie(title='13 Going On 30', duration=98, rating=6, description='A girl makes a wish on her thirteenth birthday, and wakes up the next day as a thirty-year-old woman.', mood='cheerful, humorous, romantic', occasion='date night, alone time')
            thirteen_key = thirteen.put()
            buy = Movie(title="Can't Buy Me Love", duration=94, rating=7, description='A nerdy outcast secretly pays the most popular girl in school one thousand dollars to be his girlfriend.', mood='mellow, nostalgic, humorous', occasion='date night, alone time')
            buy_key = buy.put()
            tendays = Movie(title='How to Lose a Guy in 10 Days', duration=96, rating=6, description="Benjamin Barry is an advertising executive and ladies' man who, to win a big campaign, bets that he can make a woman fall in love with him in 10 days. Andie Anderson covers the 'How To' beat for 'Composure' magazine and is assigned to write an article on 'How to Lose a Guy in 10 days.'", mood='romantic, humorous, cheerful', occasion='date night, indecisive, casual watching')
            tendays_key = tendays.put()
            mulan = Movie(title='Mulan', duration=88, rating=8, description="To save her father from death in the army, a young maiden secretly goes in his place and becomes one of China's greatest heroines in the process.", mood='nostalgic, energetic, mellow', occasion='indecisive, family night, casual watching')
            mulan_key = mulan.put()
            prince = Movie(title='A Christmas Prince', duration=92, rating=6, description='When a reporter goes undercover as a tutor to get the inside scoop on a playboy prince, she gets tangled in some royal intrigue and ends up finding love - but will she be able to keep up her lie?', mood='humorous, romantic', occasion='christmas, alone time, indecisive')
            prince_key = prince.put()
            kissmas = Movie(title='Merry Kissmas', duration=89, rating=6, description='A woman engaged to marry a self-centered film and stage director/choreographer falls for a caterer whom she kisses, as does he for her.', mood=' romantic, humorous,', occasion='christmas, alone time')
            kissmas_key = kissmas.put()
            bolt = Movie(title='Bolt', duration=96, rating=7, description='The canine star of a fictional sci-fi/action show that believes his powers are real embarks on a cross country trek to save his co-star from a threat he believes is just as real.', mood='energetic, gloomy', occasion='indecisive, playdate, family night')
            bolt_key = bolt.put()
            angels = Movie(title='Angels in the Snow', duration=90, rating=6, description='When nothing short of a miracle can hold a deteriorating family together, a Christmas getaway sets the stage for a miracle to occur. A heartwarming family story of love, loss and rediscovery.', mood='energetic, humorous', occasion='christmas, family night')
            angels_key = angels.put()
            tarzan = Movie(title='Tarzan', duration=88, rating=7, description='A man raised by gorillas must decide where he really belongs when he discovers he is a human.', mood='nostalgic, energetic', occasion='family night, casual watching, playdate')
            tarzan_key = tarzan.put()
            spooky = Movie(title='Spooky Buddies', duration=88, rating=5, description='The puppies go on a spooky adventure through a haunted mansion.', mood='cheerful, mellow, humorous', occasion='halloween, family night, playdate')
            spooky_key = spooky.put()
            cap3 = Movie(title='Captain America: Civil War', duration=148, rating=8, description="Political involvement in the Avengers' activities causes a rift between Captain America and Iron Man.", mood='energetic', occasion='feeling super, alone time, casual watching, indecisive')
            cap3_key = cap3.put()
            frosty = Movie(title='The Legend of Frosty the Snowman', duration=67, rating=5, description='Frosty the Snowman goes where he is needed most, and the town of Evergreen sure needs a visit.', mood='inspirational, nostalgic, cheerful', occasion='casual watching, christmas')
            frosty_key = frosty.put()
            ghostbusters = Movie(title='Ghostbusters', duration=105, rating=8, description='Three former parapsychology professors set up shop as a unique ghost removal service.', mood='nostalgic, humorous, mellow', occasion='halloween, casual watching')
            ghostbusters_key = ghostbusters.put()
            guardians2 = Movie(title='Guardians of the Galaxy 2', duration=136, rating=8, description="The Guardians must fight to keep their newfound family together as they unravel the mystery of Peter Quill's true parentage.", mood='humorous, energetic, gloomy, cheerful', occasion='casual watching, alone time, feeling super, indecisive')
            guardians2_key = guardians2.put()
        else:
            pass
            # print("deleting movies")
            # movie_list = Movie.query().fetch(keys_only = True)
            # ndb.delete_multi(movie_list)
            # shrek = Movie(title='Shrek', duration=123, rating=10, description='About an ogre who lives in a swamp.', mood='humorous', occasion='family night')
            # shrek_key = shrek.put()
            # print("adding movies")
            # thor = Movie(title='Thor: Ragnarok', duration=130, rating=8, description='Thor is imprisoned on the planet Sakaar, and must race against time to return to Asgard and stop Ragnarok, the destruction of his world, at the hands of the powerful and ruthless villain Hela.', mood='humorous, cheerful', occasion='casual watching')
            # thor_key = thor.put()
            # wake = Movie(title='Before I wake', duration=97, rating=6, description='A couple adopt an orphaned child whose dreams - and nightmares - manifest physically as he sleeps.', mood='gloomy', occasion='halloween based')
            # wake_key = wake.put()
            # santa = Movie(title='Santa Buddies', duration=88, rating=5, description='At the North Pole, Santa Claus (Father Christmas) and his chief dog Santa Paws worry as the whole toy processing system is threatened by the weakening of its magical power source, the icicle drawing on Christmas spirit.', mood='cheerful', occasion='Christmas')
            # santa_key = santa.put()
            # pounds = Movie(title='Seven Pounds', duration=123, rating=8, description='A man with a fateful secret embarks on an extraordinary journey of redemption by forever changing the lives of seven strangers.', mood='inspirational', occasion='casual watching')
            # pounds_key = pounds.put()
        movie_query = Movie.query()
        all_movies = movie_query.fetch()
        rec_movies = []
        movie_posters = []
        for movie in all_movies:
            if (mood in movie.mood) and (occasion in movie.occasion):
                print "movie found!!!!!!"
                # rec_movies.append(movie)
                url = "https://api.themoviedb.org/3/search/movie?api_key=15d2ea6d0dc1d476efbca3eba2b9bbfb&query="
                result = urlfetch.fetch(url + urllib.quote_plus(movie.title))
                print(result.content)
                results_json = json.loads(result.content)
                results = results_json["results"]
                firstresult = results[0]
                poster_url = "http://image.tmdb.org/t/p/w500" + firstresult["poster_path"]
                # movie_posters.append(poster_url)
                print(results_json['total_results'])
                print(poster_url)
                rec_movies.append({
                    "movie": movie,
                    "poster": poster_url,
                })
        movie_dic = {
            "movies": rec_movies,
            # "posters": movie_posters,
        }
        print(movie_posters)
        result_template = the_jinja_environment.get_template('templates/result.html')
        self.response.write(result_template.render(movie_dic))


class AboutPage(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_environment.get_template('templates/about.html')
        self.response.write(welcome_template.render())
    def post(self):
        result_template = the_jinja_environment.get_template('templates/about.html')
        self.response.write(result_template.render())

app = webapp2.WSGIApplication([
    ('/', WelcomePage),
    # ('/loading', Upload),
    ('/result', ResultPage),
    ('/about', AboutPage),
], debug=True)
