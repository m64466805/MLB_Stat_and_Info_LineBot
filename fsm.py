from transitions.extensions import GraphMachine
from utils import send_image_carousel, send_button_message, send_button_carousel, showGames, yesterGames, push_message_own, scrapeBoxscore, searchplayer, searchteam, showstanding, statleader, showschedule, showmeme, shownews, searchgame

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_lobby(self, event):
        text = event.message.text
        return True

    def is_going_to_testing(self, event):
        text = event.message.text
        return text.lower() == "testing"
    
    def is_going_to_searchplayer(self, event):
        text = event.message.text
        return text.lower() == "search player"

    def is_going_to_watchGame(self, event):
        text = event.message.text
        return text.lower() == "watch game"

    def is_going_to_todayGame(self, event):
        text = event.message.text
        return text.lower() == "today game"

    def is_going_to_yesterGame(self, event):
        text = event.message.text
        return text.lower() == "yesterday game"

    def is_going_to_searchgame(self, event):
        text = event.message.text
        return text.lower() == "search game"

    def is_going_to_showsearchgame(self, event):
        text = event.message.text
        return True
    
    def is_going_to_showplayer(self, event):
        return True

    def is_going_to_showstanding(self, event):
        text = event.message.text
        return text.lower() == "show standing"

    def is_going_to_gameBoxscore(self, event):
        text = event.message.text
        return text.lower() == "game box score"

    def is_going_to_showBoxscore(self, event):
        return True

    def is_going_to_backLobby(self, event):
        text = event.message.text
        return text.lower() == "no"

    def is_going_to_boxfromgame(self, event):
        text = event.message.text
        return text.lower() == "yes"

    def is_going_to_searchteam(self, event):
        text = event.message.text
        return text.lower() == "search team"

    def is_going_to_showteam(self, event):
        return True

    def is_going_to_statleader(self, event):
        text = event.message.text
        return text.lower() == "stat leader"

    def is_going_to_showschedule(self, event):
        text = event.message.text
        return text.lower() == "show schedule"

    def is_going_to_showmeme(self, event):
        text = event.message.text
        return text.lower() == "show Meme"

    def is_going_to_shownews(self, event):
        text = event.message.text
        return text.lower() == "show news"

    def on_enter_lobby(self, event):
        userid = event.source.user_id
        send_button_carousel(userid)

    def on_enter_testing(self, event):
        print("I am entering Testing")
        # test
        userid = event.source.user_id

        url1 = 'https://cdn.discordapp.com/attachments/943146710589399145/1054056604498141214/aaron-judge-62.png'
        title = 'title'
        uptext = 'uptext'
        labels = ['yes', 'no']
        texts = ['yes', 'no']
        send_button_message(userid, url1, title, uptext, labels, texts)
        # send_news_carousel(userid, urls, labels, urls)
        # send_image_map(userid)
        self.go_back(event)

    def on_enter_searchplayer(self, event):
        print("I an entering searchplayer")
        reply_token = event.reply_token
        userid = event.source.user_id

        S_Ohtani= 'https://media.discordapp.net/attachments/943146710589399145/1054062223707881492/Shohei_Ohtani.jpg'
        B_Harper= 'https://cdn.discordapp.com/attachments/943146710589399145/1054062135677833226/Bryce_Harper.jpg'
        C_Correa= 'https://cdn.discordapp.com/attachments/943146710589399145/1054062154992590998/Carlos_Correa.jpg'
        G_Cole= 'https://cdn.discordapp.com/attachments/943146710589399145/1054062177541177424/Gerrit_Cole.jpg'
        M_Betts= 'https://cdn.discordapp.com/attachments/943146710589399145/1054062206855159829/Mookie_Betts.jpg'
        urls = [S_Ohtani, B_Harper, C_Correa, G_Cole, M_Betts]
        labels = ['Shohei_Ohtani', 'Bryce_Harper', 'Carlos_Correa', 'Gerrit_Cole', 'Mookie_Betts']
        texts = ['Shohei Ohtani', 'Bryce Harper', 'Carlos Correa', 'Gerrit Cole', 'Mookie Betts']
        send_image_carousel(userid, urls, labels, texts)

        msg= "Press on the ALLSTAR above or enter a player name"
        push_message_own(userid, msg)

    def on_enter_watchGame(self, event):
        print("I am entering watchGame")

        reply_token = event.reply_token
        userid = event.source.user_id

        img= 'https://cdn.discordapp.com/attachments/943146710589399145/1054067432374943814/gametoday.png'
        title = 'Watch game scores'
        uptext = 'Which day would you like to watch?'
        labels = ['Game today', 'Game yesterday']
        texts = ['today game', 'yesterday game', 'search game']
        send_button_message(userid, img, title, uptext, labels, texts)

    def on_enter_todayGame(self, event):
        print("I am entering todayGame")
        reply_token = event.reply_token
        userid = event.source.user_id
        showGames(userid,reply_token)

        img ='https://cdn.discordapp.com/attachments/943146710589399145/1054068838163038329/gameday.png'
        title = 'Watch more'
        uptext = 'Check out game result or back to menu?'
        labels = ['Game result', 'Back to menu']
        texts = ['yes','no']
        send_button_message(userid, img, title, uptext, labels, texts)

    def on_enter_yesterGame(self, event):
        print("I am entering yesterGame")
        reply_token = event.reply_token
        userid = event.source.user_id
        yesterGames(userid,reply_token)

        img= 'https://cdn.discordapp.com/attachments/943146710589399145/1054068838163038329/gameday.png'
        title = 'Watch more'
        uptext = 'Check out game result or back to menu?'
        labels = ['Game result', 'Back to menu']
        texts = ['yes', 'no']
        send_button_message(userid, img, title, uptext, labels, texts)

    def on_enter_showplayer(self, event):
        print("I am entering showplayer")
        userid = event.source.user_id
        reply_token = event.reply_token
        playername = event.message.text
        try:
            push_message_own(userid,"Enter Player Name: ")
            searchplayer(reply_token, userid, playername)
            img= 'https://cdn.discordapp.com/attachments/943146710589399145/1054070400377684038/2022_allstar.png'
            title= 'Watch more'
            uptext= 'Please choose'
            labels= ['Search more players', 'Search team', 'Back to menu']
            texts= ['search player', 'search team', 'no']
            send_button_message(userid, img, title, uptext, labels, texts)
        except:
            push_message_own(userid,"Player not found, check format or your brain, then try again")
            self.go_back(event)

    def on_enter_gameBoxscore(self, event):
        print("I am entering gameBoxscore")
        reply_token = event.reply_token
        userid = event.source.user_id
        #push_message_own(userid, "Please enter date and team, Ex: July 15, 2022 New York Yankees")

    def on_enter_showBoxscore(self, event):
        print("I am entering showBoxscore")
        reply_token = event.reply_token
        userid = event.source.user_id
        msg = event.message.text
        try:
            scrapeBoxscore(userid, msg)
            img= 'https://cdn.discordapp.com/attachments/943146710589399145/1054070400377684038/2022_allstar.png'
            title= 'Watch more'
            uptext= 'Please choose'
            labels= ['Search player', 'Search team', 'Back to menu']
            texts= ['search player', 'search team', 'no']
            send_button_message(userid, img, title, uptext, labels, texts)
        except:
            push_message_own(userid, "Wrong format, please try again")
            self.go_back(event)

    def on_enter_searchteam(self, event):
        print("I am entering searchteam")
        reply_token = event.reply_token
        userid = event.source.user_id

        Yankees= 'https://cdn.discordapp.com/attachments/943146710589399145/1054106443109912607/Yankees.jpg'
        Dodgers= 'https://cdn.discordapp.com/attachments/943146710589399145/1054106781216952390/Dodgers.jpg'
        Astros= 'https://cdn.discordapp.com/attachments/943146710589399145/1054107085702447134/astros.jpg'
        Braves= 'https://cdn.discordapp.com/attachments/943146710589399145/1054107283279331369/braves.png'
        RedSox= 'https://cdn.discordapp.com/attachments/943146710589399145/1054107471251259483/redsox.jpg'

        urls = [Yankees, Dodgers, Astros, Braves, RedSox]
        labels =['Yankees','Dodgers', 'Astros', 'Braves', 'Redsox']
        texts = ['New York Yankees', 'Los Angeles Dodgers', 'Houston Astros', 'Atlanta Braves', 'Boston Red Sox']
        send_image_carousel(userid, urls, labels, texts)

        msg = "Press on the hot teams above or enter a team name"
        push_message_own(userid, msg)
    
    def on_enter_showteam(self, event):
        print("I am entering showteam")
        userid = event.source.user_id
        reply_token = event.reply_token
        teamname = event.message.text
        try:
            searchteam(reply_token, userid, teamname)
            img= 'https://cdn.discordapp.com/attachments/943146710589399145/1054070400377684038/2022_allstar.png'
            title = 'Watch more'
            uptext = 'Please choose'
            labels = ['Search player', 'Search more teams', 'Back to menu']
            texts = ['search player', 'search team', 'no']
            send_button_message(userid, img, title, uptext, labels, texts)
        except:
            push_message_own(userid, "No this team or wrong format, please try again")
            self.go_back(event)

    def on_enter_showstanding(self, event):
        print("I am entering showstanding")
        userid = event.source.user_id
        showstanding(userid)
        
        img= 'https://cdn.discordapp.com/attachments/943146710589399145/1054105901411340469/mlb.png'
        title = 'Watch more'
        uptext = 'Search more teams or back to menu'
        labels = ['Search team', 'Back to menu']
        texts = ['search team', 'no']
        send_button_message(userid, img, title, uptext, labels, texts)

    def on_enter_statleader(self, event):
        print("I am entering statleader")
        userid = event.source.user_id
        statleader(userid)
        
        img= 'https://cdn.discordapp.com/attachments/943146710589399145/1054070400377684038/2022_allstar.png'
        title = 'Watch more'
        uptext = 'Search for player or back to menu'
        labels = ['Search player', 'back to menu']
        texts= ['search player', 'no']
        send_button_message(userid, img, title, uptext, labels, texts)

    def on_enter_showschedule(self, event):
        print("I am entering showschedule")
        userid = event.source.user_id
        showschedule(userid)

        img= 'https://cdn.discordapp.com/attachments/943146710589399145/1054105281895858197/2023schedule.jpg'
        title= 'Watch more'
        uptext= 'Search for team or back to menu'
        labels= ['Search team', 'Back to menu']
        texts= ['search team', 'no']
        send_button_message(userid, img, title, uptext, labels ,texts)

    def on_enter_showmeme(self, event):
        print('I am entering showmeme')
        userid = event.source.user_id
        try:
            showmeme(userid)
            img= 'https://cdn.discordapp.com/attachments/943146710589399145/1054104875492982835/Baseball.jpg'
            title = 'Watch more'
            uptext= 'Watch MLB News or back to menu'
            labels= ['MLB news', 'Back to menu']
            texts= ['yes', 'no']
            send_button_message(userid, img, title, uptext, labels, texts)
        except:
            push_message_own(userid, "Network error, please try again")
            self.go_back(event)
    
    def on_enter_shownews(self, event):
        print("I am entering shownews")
        userid = event.source.user_id
        shownews(userid)

        img= 'https://cdn.discordapp.com/attachments/943146710589399145/1054104660341964810/breakingnew.jpg'
        title= 'Watch more'
        uptext= 'Find Meme or back to menu'
        labels= ['Meme', 'Back to Menu']
        texts= ['yes', 'no']
        send_button_message(userid, img, title, uptext, labels, texts)

    def on_enter_searchgame(self, event):
        print("I am entering searchgame")
        reply_token = event.reply_token
        userid = event.source.user_id
        msg= "Please enter the date of the game that you want to watch, Ex: July 5,2022"
        push_message_own(userid,msg)

    def on_enter_showsearchgame(self, event):
        print("I am entering showsearchgame")
        userid = event.source.user_id
        date = event.message.text
        reply_token = event.reply_token

        try:
            searchgame(reply_token, date)
            img= 'https://cdn.discordapp.com/attachments/943146710589399145/1054068838163038329/gameday.png'
            title= 'Watch more'
            uptext= 'Watch game result or back to menu'
            labels= ['Game result', 'Back to menu']
            texts= ['yes','no']
            send_button_message(userid, img, title, uptext, labels, texts)
        except:
            push_message_own(userid, "Wrong format, please try again")
            self.go_back(event)