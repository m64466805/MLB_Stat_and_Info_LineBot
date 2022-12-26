import os
from linebot import LineBotApi
# from linebot import LineBotApi, WebhookParser
# from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage,TemplateSendMessage,ImageCarouselColumn,ImageCarouselTemplate,URITemplateAction
from linebot.models import TextSendMessage, ImageSendMessage, TemplateSendMessage, ImageCarouselColumn, ImageCarouselTemplate, ButtonsTemplate, MessageTemplateAction, URITemplateAction, ImageSendMessage, CarouselTemplate, CarouselColumn
import pybaseball
import statsapi


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(channel_access_token)

#Done
def send_text_message(reply_token, text):
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

#Done
def send_image_url(id, img_url):
    message = ImageSendMessage(
        original_content_url=img_url,
        preview_image_url=img_url
    )
    line_bot_api.reply_message(id, message)

    return "OK"

#Done
def send_video_url(id):
    message = ImageSendMessage(
        original_content_url= 'https://youtu.be/xCD0yKdvOZo',
        preview_image_url= 'https://cdn.discordapp.com/attachments/943146710589399145/1054062121580765214/Aaron_Judge.jpg'
    )
    line_bot_api.push_message(id, message)
    return "OK"

#Done
def send_template_message(id, imglinks):
    cols = []
    for i, url in enumerate(imglinks):
        cols.append(
            ImageCarouselColumn(
                image_url=url,
                action= URITemplateAction(
                    label= 'Meme',
                    uri=url
                )
            )
        )
    message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(columns=cols)
    )
    line_bot_api.push_message(id, message)
    return "OK"
#Done
def send_image_carousel(id, imglinks, labels, texts):
    cols = []
    for i, url in enumerate(imglinks):
        cols.append(
            ImageCarouselColumn(
                image_url= url,
                action= MessageTemplateAction(
                    label= labels[i],
                    text= texts[i]
                )
            )
        )
    message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(columns=cols)
    )
    line_bot_api.push_message(id, message)
    return "OK"

#Done
def send_button_message(id, img, title, uptext, labels, texts):

    acts = []
    for i, lab in enumerate(labels):
        acts.append(
            MessageTemplateAction(
                label=lab,
                text=texts[i]
            )
        )
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url=img,
            title=title,
            text=uptext,
            actions=acts
        )
    )
    line_bot_api.push_message(id, message)
    return "OK"

#Done
def send_button_carousel(id):
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url= 'https://cdn.discordapp.com/attachments/943146710589399145/1054062121580765214/Aaron_Judge.jpg',
                    title= 'Daily MLB Menu 1',
                    text='What would you like to watch?',
                    actions=[
                        MessageTemplateAction(
                            label= 'Watch Game',
                            text= 'watch game'
                        ),
                        MessageTemplateAction(
                            label= 'Standing',
                            text= 'show standing'
                        ),
                        MessageTemplateAction(
                            label= 'Game Schedule',
                            text= 'show schedule'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url= 'https://cdn.discordapp.com/attachments/943146710589399145/1054062206855159829/Mookie_Betts.jpg',
                    title= 'Daily MLB Menu 2',
                    text='What would you like to watch?',
                    actions=[
                        MessageTemplateAction(
                            label= 'Stat leader',
                            text= 'stat leader'
                        ),
                        MessageTemplateAction(
                            label= 'Game Result',
                            text= 'game box score'
                        ),
                        MessageTemplateAction(
                            label= 'Search Player',
                            text= 'search player'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url= 'https://cdn.discordapp.com/attachments/943146710589399145/1054062223707881492/Shohei_Ohtani.jpg',
                    title= 'Daily MLB Menu 3',
                    text='What would you like to watch?',
                    actions=[
                        MessageTemplateAction(
                            label= 'Search Team',
                            text= 'search team'
                        ),
                        MessageTemplateAction(
                            label= 'MLB news',
                            text= 'show news'
                        ),
                        URITemplateAction(
                            label= 'MLB_Highlights',
                            uri='https://www.youtube.com/@MLB'
                        )
                    ]
                ),
            ]
        )
    )
    line_bot_api.push_message(id, message)
    return "OK"
#half done
def send_news_carousel(id, imglinks, titles, links):
    cols = []
    for i, img in enumerate(imglinks):
        cols.append(
            CarouselColumn(
                thumbnail_image_url= img,
                title= 'MLB news',
                text=titles[i],
                actions=[
                    URITemplateAction(
                        label= 'Read more',
                        uri= links[i]
                    )
                ]
            )
        )
    message= TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(columns=cols)
    )
    line_bot_api.push_message(id, message)
    return "OK"

def get_team_id(team):
    teamget= statsapi.lookup_team(team)
    team_id= []
    for id_ in teamget:
        team_id.append(id_['id'])
    return team_id
def get_player_id(player):
    playerget= statsapi.lookup_player(player)
    player_id= []
    for id_ in playerget:
        player_id.append(id_['id'])
    return player_id
#done
def showGames(userid,reply_token):
    push_message_own(userid,'Cleveland Guardians: No Game today')
    push_message_own(userid,'Detroit Tigers: No Game today')
    push_message_own(userid,'Kansas City Royals: No Game today')
    push_message_own(userid,'Minnesota Twins: No Game today')
    push_message_own(userid,'Chicago Cubs: No Game today')
    push_message_own(userid,'Cincinnati Reds: No Game today')
    push_message_own(userid,'Milwaukee Brewers: No Game today')
    push_message_own(userid,'Pittsburgh Pirates: No Game today')
    push_message_own(userid,'St. Louis Cardinals: No Game today')
    push_message_own(userid,'Baltimore Orioles: No Game today')
    push_message_own(userid,'Boston Red Sox: No Game today')
    push_message_own(userid,'New York Yankees: No Game today')
    push_message_own(userid,'Tampa Bay Rays: No Game today')
    push_message_own(userid,'Toronto Blue Jays: No Game today')
    push_message_own(userid,'Atlanta Braves: No Game today')
    push_message_own(userid,'Miami Marlins: No Game today')
    push_message_own(userid,'New York Mets: No Game today')
    push_message_own(userid,'Philadelphia Phillies: No Game today')
    push_message_own(userid,'Washington Nationals: No Game today')
    push_message_own(userid,'Houston Astros: No Game today')
    push_message_own(userid,'Los Angeles Angels: No Game today')
    push_message_own(userid,'Oakland Athletics: No Game today')
    push_message_own(userid,'Seattle Mariners: No Game today')
    push_message_own(userid,'Texas Rangers: No Game today')
    push_message_own(userid,'Arizona Diamondbacks: No Game today')
    push_message_own(userid,'Colorado Rockies: No Game today')
    push_message_own(userid,'Los Angeles Dodgers: No Game today')
    push_message_own(userid,'San Diego Padres: No Game today')
    push_message_own(userid,'San Francisco Giants: No Game today')

#done
def yesterGames(userid,reply_token):
    push_message_own(userid,'Show all team last game score: ')

    result=get_team_id('CLE')
    last=statsapi.last_game(result[0])    
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'Cleveland Guardians: ')
    push_message_own(userid,yesgame)
    
    result=get_team_id('DET')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'Detroit Tigers: ')
    push_message_own(userid,yesgame)

    result=get_team_id('KC')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'Kansas City Royals: ')
    push_message_own(userid,yesgame)
    
    result=get_team_id('MIN')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'Minnesota Twins: ')
    push_message_own(userid,yesgame)
    
    result=get_team_id('CHC')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'Chicago Cubs: ')
    push_message_own(userid,yesgame)
    
    result=get_team_id('CIN')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'Cincinnati Reds: ')
    push_message_own(userid,yesgame)

    result=get_team_id('MIL')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'Milwaukee Brewers: ')
    push_message_own(userid,yesgame)

    result=get_team_id('PIT')
    last=statsapi.last_game(result[0])    
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'Pittsburgh Pirates: ')
    push_message_own(userid,yesgame)

    result=get_team_id('STL')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'St. Louis Cardinals: ')
    push_message_own(userid,yesgame)

    result=get_team_id('BAL')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'Baltimore Orioles: ')
    push_message_own(userid,yesgame)

    result=get_team_id('BOS')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'Boston Red Sox: ')
    push_message_own(userid,yesgame)

    result=get_team_id('NYY')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'New York Yankees: ')
    push_message_own(userid,yesgame)

    result=get_team_id('TB')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'Tampa Bay Rays: ')
    push_message_own(userid,yesgame)

    result=get_team_id('TOR')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'Toronto Blue Jays: ')
    push_message_own(userid,yesgame)

    result=get_team_id('ATL')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'Atlanta Braves: ')
    push_message_own(userid,yesgame)

    result=get_team_id('MIA')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'Miami Marlins: ')
    push_message_own(userid,yesgame)    

    result=get_team_id('NYM')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'New York Mets: ')
    push_message_own(userid,yesgame)

    result=get_team_id('PHI')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'Philadelphia Phillies: ')
    push_message_own(userid,yesgame)

    result=get_team_id('WAS')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'Washington Nationals: ')
    push_message_own(userid,yesgame)

    result=get_team_id('HOU')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'Houston Astros: ')
    push_message_own(userid,yesgame)

    result=get_team_id('ANA')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'Los Angeles Angels: ')
    push_message_own(userid,yesgame)

    result=get_team_id('OAK')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'Oakland Athletics: ')
    push_message_own(userid,yesgame)


    result=get_team_id('SEA')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'Seattle Mariners: ')
    push_message_own(userid,yesgame)

    result=get_team_id('TEX')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'Texas Rangers: ')
    push_message_own(userid,yesgame)

    result=get_team_id('D-backs')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'Arizona Diamondbacks: ')
    push_message_own(userid,yesgame)

    result=get_team_id('COL')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'Colorado Rockies: ')
    push_message_own(userid,yesgame)

    result=get_team_id('LAN')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'Los Angeles Dodgers: ')
    push_message_own(userid,yesgame)

    result=get_team_id('SD')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'San Diego Padres: ')
    push_message_own(userid,yesgame)

    result=get_team_id('SF')
    last=statsapi.last_game(result[0])
    yesgame= statsapi.linescore(last)
    push_message_own(userid,'San Francisco Giants: ')
    push_message_own(userid,yesgame)


def scrapeBoxscore(userid, dateteam):
    #result= statsapi.boxscore(565997, battingBox=True, battingInfo=True, fieldingInfo=True, pitchingBox=True, gameInfo=True)
    push_message_own(userid, 'Go here to search Boxscore')
    push_message_own(userid,'https://www.mlb.com/scores')

def searchplayer(reply_token, userid, playertofind):
    #result= statsapi.lookup_player(playertofind)
    result_id= get_player_id(playertofind)
    player=statsapi.player_stats(result_id[0],'hitting','career')
    push_message_own(userid, player)
    player=statsapi.player_stats(result_id[0],'pitching','career')
    push_message_own(userid, player)
    player=statsapi.player_stats(result_id[0],'fielding','career')
    push_message_own(userid, player)
    # player=statsapi.player_stats(result_id[0],'hitting','career')
    # push_message_own(userid, 'Go here to search player')
    # push_message_own(userid, 'https://www.baseball-reference.com/')
#done
def searchteam(reply_token, userid, teamtofind):
    result_id= get_team_id(teamtofind)
    walks= statsapi.team_leaders(result_id[0],'walks',limit=5,season=2022)
    homerun=statsapi.team_leaders(result_id[0],'homeRuns',limit=5,season=2022)
    inningsPitched=statsapi.team_leaders(result_id[0],'inningsPitched',limit=5,season=2022)
    battingAverage=statsapi.team_leaders(result_id[0],'battingAverage',limit=5,season=2022)
    earnedRunAverage=statsapi.team_leaders(result_id[0],'earnedRunAverage',limit=5,season=2022)
    push_message_own(userid, walks)
    push_message_own(userid, homerun)
    push_message_own(userid, battingAverage)
    push_message_own(userid, inningsPitched)
    push_message_own(userid, earnedRunAverage)


# done
#pybaseball can get it
def showstanding(userid):

    season_data = statsapi.latest_season()
    print(season_data['seasonId'])
    push_message_own(userid,'AL:')
    # result= statsapi.standings(leagueId=103,include_wildcard=False,season=season_data['seasonId'])
    result= statsapi.standings(leagueId=103,include_wildcard=False,season=2022)
    print(result)
    push_message_own(userid, result)
    push_message_own(userid,'NL:')
    # result= statsapi.standings(leagueId=104,include_wildcard=False,season=season_data['seasonId'])
    result= statsapi.standings(leagueId=104,include_wildcard=False,season=2022)
    print(result)
    push_message_own(userid, result)

# done
def statleader(userid):

    season_data = statsapi.latest_season()
    print(season_data['seasonId'])
    push_message_own(userid, 'OPS Leader:')
    # OPSLeader= statsapi.league_leaders('onBasePlusSlugging',statGroup='hitting',limit= 10, season=season_data['seasonId'])
    OPSLeader= statsapi.league_leaders('onBasePlusSlugging',statGroup='hitting',limit= 10, season=2022)
    push_message_own(userid, OPSLeader)

    push_message_own(userid, 'HR King:')
    # HRLeader= statsapi.league_leaders('homeRuns',statGroup='hitting',limit= 10, season=season_data['seasonId'])
    HRLeader= statsapi.league_leaders('homeRuns',statGroup='hitting',limit= 10, season=2022)
    push_message_own(userid, HRLeader)

    push_message_own(userid, 'Batting Average:')
    # BattingAverageLeader= statsapi.league_leaders('battingAverage', statGroup='hitting', limit=10, season=season_data['seasonId'])
    BattingAverageLeader= statsapi.league_leaders('battingAverage', statGroup='hitting', limit=10, season=2022)
    push_message_own(userid, BattingAverageLeader)

    push_message_own(userid, 'ERA King:')
    # ERALeader= statsapi.league_leaders('earnedRunAverage',statGroup='pitching',limit=10, season=season_data['seasonId'])
    ERALeader= statsapi.league_leaders('earnedRunAverage',statGroup='pitching',limit=10, season=2022)
    push_message_own(userid, ERALeader)

    push_message_own(userid, 'PitchInnings King:')
    # PitchInningsLeader= statsapi.league_leaders('inningsPitched',statGroup='pitching',limit=10, season=season_data['seasonId'])
    PitchInningsLeader= statsapi.league_leaders('inningsPitched',statGroup='pitching',limit=10, season=2022)
    push_message_own(userid, PitchInningsLeader)

#done
def showschedule(userid):
    push_message_own(userid,'Show tommorrow all team games: ')

    result=get_team_id('CLE')
    next=statsapi.next_game(result[0])
    print('Cleveland Guardians')
    print(next)    
    push_message_own(userid,'Cleveland Guardians: ')
    push_message_own(userid,'No game tommorow')

    result=get_team_id('DET')
    next=statsapi.next_game(result[0])
    print('Detroit Tigers')
    print(next)    
    push_message_own(userid,'Detroit Tigers: ')
    push_message_own(userid,'No game tommorow')

    result=get_team_id('KC')
    next=statsapi.next_game(result[0])
    print('Kansas City Royals')
    print(next)     
    push_message_own(userid,'Kansas City Royals: ')
    push_message_own(userid,'No game tommorow')

    result=get_team_id('MIN')
    next=statsapi.next_game(result[0])
    print('Minnesota Twins')
    print(next)    
    push_message_own(userid,'Minnesota Twins: ')
    push_message_own(userid,'No game tommorow')

    result=get_team_id('CHC')
    next=statsapi.next_game(result[0])
    print('Chicago Cubs')
    print(next)    
    push_message_own(userid,'Chicago Cubs: ')
    push_message_own(userid,'No game tommorow')

    result=get_team_id('CIN')
    next=statsapi.next_game(result[0])
    print('Cincinnati Reds')
    print(next) 
    push_message_own(userid,'Cincinnati Reds: ')
    push_message_own(userid,'No game tommorow')
   
    result=get_team_id('MIL')
    next=statsapi.next_game(result[0])
    print('Milwaukee Brewers')
    print(next)    
    push_message_own(userid,'Milwaukee Brewers: ')
    push_message_own(userid,'No game tommorow')

    result=get_team_id('PIT')
    next=statsapi.next_game(result[0])
    print('Pittsburgh Pirates')
    print(next)    
    push_message_own(userid,'Pittsburgh Pirates: ')
    push_message_own(userid,'No game tommorow')

    result=get_team_id('STL')
    next=statsapi.next_game(result[0])
    print('St. Louis Cardinals')
    print(next)    
    push_message_own(userid,'St. Louis Cardinals: ')
    push_message_own(userid,'No game tommorow')

    result=get_team_id('BAL')
    next=statsapi.next_game(result[0])
    print('Baltimore Orioles')
    print(next)    
    push_message_own(userid,'Baltimore Orioles: ')
    push_message_own(userid,'No game tommorow')

    result=get_team_id('BOS')
    next=statsapi.next_game(result[0])
    print('Boston Red Sox')
    print(next)    
    push_message_own(userid,'Boston Red Sox: ')
    push_message_own(userid,'No game tommorow')

    result=get_team_id('NYY')
    next=statsapi.next_game(result[0])
    print('New York Yankees')
    print(next)    
    push_message_own(userid,'New York Yankees: ')
    push_message_own(userid,'No game tommorow')

    result=get_team_id('TB')
    next=statsapi.next_game(result[0])
    print('Tampa Bay Rays')
    print(next)    
    push_message_own(userid,'Tampa Bay Rays: ')
    push_message_own(userid,'No game tommorow')

    result=get_team_id('TOR')
    next=statsapi.next_game(result[0])
    print('Toronto Blue Jays')
    print(next)    
    push_message_own(userid,'Toronto Blue Jays: ')
    push_message_own(userid,'No game tommorow')

    result=get_team_id('ATL')
    next=statsapi.next_game(result[0])
    print('Atlanta Braves')
    print(next)    
    push_message_own(userid,'Atlanta Braves: ')
    push_message_own(userid,'No game tommorow')

    result=get_team_id('MIA')
    next=statsapi.next_game(result[0])
    print('Miami Marlins')
    print(next)       
    push_message_own(userid,'Miami Marlins: ')
    push_message_own(userid,'No game tommorow')

    result=get_team_id('NYM')
    next=statsapi.next_game(result[0])
    print('New York Mets')
    print(next)    
    push_message_own(userid,'New York Mets: ')
    push_message_own(userid,'No game tommorow')

    result=get_team_id('PHI')
    next=statsapi.next_game(result[0])
    print('Philadelphia Phillies')
    print(next)     
    push_message_own(userid,'Philadelphia Phillies: ')
    push_message_own(userid,'No game tommorow')

    result=get_team_id('WAS')
    next=statsapi.next_game(result[0])
    print('Washington Nationals')
    print(next)    
    push_message_own(userid,'Washington Nationals: ')
    push_message_own(userid,'No game tommorow')

    result=get_team_id('HOU')
    next=statsapi.next_game(result[0])
    print('Houston Astros')
    print(next)      
    push_message_own(userid,'Houston Astros: ')
    push_message_own(userid,'No game tommorow')

    result=get_team_id('ANA')
    next=statsapi.next_game(result[0])
    print('Los Angeles Angels')
    print(next)   
    push_message_own(userid,'Los Angeles Angels: ')
    push_message_own(userid,'No game tommorow')

    result=get_team_id('OAK')
    next=statsapi.next_game(result[0])
    print('Oakland Athletics')
    print(next)     
    push_message_own(userid,'Oakland Athletics: ')
    push_message_own(userid,'No game tommorow')

    result=get_team_id('SEA')
    next=statsapi.next_game(result[0])
    print('Seattle Mariners')
    print(next)    
    push_message_own(userid,'Seattle Mariners: ')
    push_message_own(userid,'No game tommorow')

    result=get_team_id('TEX')
    next=statsapi.next_game(result[0])
    print('Texas Rangers')
    print(next)      
    push_message_own(userid,'Texas Rangers: ')
    push_message_own(userid,'No game tommorow')    
    
    result=get_team_id('D-backs')
    next=statsapi.next_game(result[0])
    print('Arizona Diamondbacks')
    print(next)    
    push_message_own(userid,'Arizona Diamondbacks: ')
    push_message_own(userid,'No game tommorow')    

    result=get_team_id('COL')
    next=statsapi.next_game(result[0])
    print('Colorado Rockies')
    print(next)     
    push_message_own(userid,'Colorado Rockies: ')
    push_message_own(userid,'No game tommorow')    

    result=get_team_id('LAN')
    next=statsapi.next_game(result[0])
    print('Los Angeles Dodgers')
    print(next)    
    push_message_own(userid,'Los Angeles Dodgers: ')
    push_message_own(userid,'No game tommorow')    

    result=get_team_id('SD')
    next=statsapi.next_game(result[0])
    print('San Diego Padres')
    print(next)    
    push_message_own(userid,'San Diego Padres: ')
    push_message_own(userid,'No game tommorow')    

    result=get_team_id('SF')
    next=statsapi.next_game(result[0])
    print('San Francisco Giants')
    print(next)      
    push_message_own(userid,'San Francisco Giants: ')
    push_message_own(userid,'No game tommorow')    

def showmeme(userid):
    push_message_own(userid,'Go Here to see some MLB Memes')
    push_message_own(userid,'https://www.facebook.com/TheMLBMemes/')
    # imglink='https://cdn.discordapp.com/attachments/943146710589399145/1054104875492982835/Baseball.jpg'
    # send_template_message(userid, imglink)

def shownews(userid):
    # imglinks= 'https://img.mlbstatic.com/mlb-images/image/upload/t_16x9/t_w1536/mlb/njajrbcksa1008hclvrj.jpg'
    # titles= 'Rumors: Conforto on several teams radar'
    # links= 'https://www.mlb.com/news/mlb-rumors-trades-and-signings?t=trades-and-transactions'
    # send_news_carousel(userid, imglinks, titles, links)
    push_message_own(userid,'https://www.mlb.com/news')

def searchgame(reply_token, date):
    month = {
        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4,
        'May': 5,
        'Jun': 6,
        'Jul': 7,
        'Aug': 8,
        'Sep': 9,
        'Oct': 10,
        'Nov': 11,
        'Dec': 12
    }
    datelist= date.split(' ')
    datelist[1] = datelist[1][:1]
    gameMonth = month[datelist[0]]
    gameYear = int(datelist[2])
    result=get_team_id('NYM')

    send_text_message(reply_token, result)


def push_message_own(userid, msg):
    line_bot_api.push_message(userid, TextSendMessage(text=msg))
    return "OK"

