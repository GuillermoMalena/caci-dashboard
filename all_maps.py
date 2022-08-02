#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def grab_maps():
    city_map = {
    'nyc': 'New York City','#NEWYORKCITY':'New York City',
    'NYC': 'New York City',
    'NY':'New York',
    'ny':'New York',
    'bronx':'Bronx',
    'brooklyn':'Brooklyn',
    'manhattan':'Manhattan',
    'bx':'Bronx',
    'bk':'Brooklyn',
    'BX':'Bronx',
    'BK':'Brooklyn',
    'queens':'Queens',
    'Queens':'Queens',
    'Brooklyn':'Brooklyn',
    'Bronx':'Bronx',
    'ATL':'Atlanta',
    'Atl':'Atlanta',
    'atl':'Atlanta',
    '𝐚𝐭𝐥':'Atlanta',
    'DET':'Detroit',
    ' LA ':'Los Angeles',
    'Houston':'Houston',
    'CT':'Connecticut',
    'New Orleans':'New Orleans',
    'NEW ORLEANS':'New Orleans',
    'GA':'Georgia',
    'Georgia':'Georgia',
    'HTX':'Houston',
    'Chicago':'Chicago',
    'BRONX':'Bronx',
    'Baltimore':'Baltimore',
    'LOUISIANA':'Louisiana',
    'Miami':'Miami',
    '305':'Miami',
    'MIA':'Miami',
    'Lansing':'Lansing',
    'D.C':'Washington DC',
    'DC':'Washington DC',
    'DMV':'DMV',
    'TX':'Texas',
    'Texan':'Texas',
    '#BROOKLYN':'Brooklyn',
    'Lake Tahoe':'Lake Tahoe','lake tahoe':'lake tahoe',
    '#DCAboveAll':'Washington DC',
    'Cleveland':'Cleveland','cleveland':'Cleveland',
    'Florida':'Florida',
    'Nashville':'Nashville','TN':'Tennessee',
    'Caracas':'Caracas',
    'Tampa':'Tampa','Tokyo':'Tokyo','tokyo':'Tokyo'
}
    nat_map = {
    #'PR': 'Puerto Rico',
    #'pr': 'Puerto Rico',
    'Puerto Rico': 'Puerto Rico', '#PUERTORICO':'Puerto Rico', 'Boricua':'Puerto Rico',
    'Haiti':'Haiti','Haitian':'Haiti',
    'Cuba':'Cuba',
    'Nigeria':'Nigeria','Nigerian':'Nigeria',
    'Jamaica':'Jamaica',
    'DR':'Dominican Republic',
    'Dominican Republic':'Dominican Republic',
    'dr':'Dominican Republic',
    'Barbados':'Barbados',
    'Trinidad & Tobago':'Trinidad & Tobago',
    'Guyana':'Guyana',
    'Pakistan':'Pakistan',
    'Mali':'Mali',
    'Grenada':'Grenada',
    'Equatorial Guinea':'Equatorial Guinea',
    'Guinea':'Guinea',
    'Ireland':'Ireland',
    'Venezuela':'Venezuela',
    'Senegal':'Senegal',
    'Netherlands':'Netherlands',
    'Denmark':'Denmark',
    'Congo - Kinshasa': 'Congo - Kinshasa',
    'Bangladesh':'Bangladesh',
    'Panama':'Panama','Panamanian':'Panama',
    'Mexico':'Mexico','Mexican':'Mexico','Chicana':'Mexico','Chicano':'Mexico',
        #'Xicana':'Mexico','Xicano':'Mexico',
    'Uruguay':'Uruguay',
    'Japan':'Japan',
    'Cyprus':'Cyprus',
    'United Kingdom':'United Kingdom',
    'El Salvador':'El Salvador',
    'Philippines':'Philippines',
    'Togo':'Togo',
    'Morocco':'Morocco',
    'Dominican':'Dominican Republic',
    'Kenyan':'Kenya',
    'South Africa':'South Africa',
    'Romania':'Romania',
    'Brazil':'Brazil','Brazilian':'Brazil',
    'Ascension Island':'Ascension Island',
    'Andorra':'Andorra',
    'United Arab Emirates':'United Arab Emirates','Emirates':'United Arab Emirates',
    'Afghanistan':'Afghanistan','Afghani':'Afghanistan',
    'Antigua & Barbuda':'Antigua & Barbuda','Antigan':'Antigua & Barbuda',
    'Anguilla':'Anguilla',
    'Albania':'Albania','Albanian':'Albania',
    'Armenia':'Armenia','Armenian':'Armenia',
    'Angola':'Angola','Angolan':'Angola',
    'Argentina':'Argentina','Argentinian':'Argentina',
    'American Samoa':'American Samoa', 'Samoan':'American Samoa',
    'Austria':'Austria','Austrian':'Austria',
    'Australia':'Australia','Aussie':'Australia',
    'Aruba':'Aruba',
    'Bangladesh':'Bangladesh','Bengali':'Bangladesh',
    'Belgium':'Belgium','Belgian':'Belgiium',
    'Bulgaria':'Bulgaria','Bulgarian':'Bulgarian',
    'Bahrain':'Bahrain','Benin':'Benin',
    'Bermuda':'Bermuda','Bolivia':'Bolivia','Bolivian':'Bolivia',
    'Bahamas':'Bahamas','Botswana':'Botswana',
    'Belize':'Belize','Canada':'Canada','Canadian':'Canada',
    'Central African Republic':'Central African Republic',
    'Switzerland':'Switzerland','Swiss':'Switzerland',
    'Chile':'Chile','Chilean':'Chile','Chileno':'Chilean',
    'Cameroon':'Cameroon','China':'China','china':'China','Chinese':'China',
    'Colombia':'Colombia','Colombian':'Colombia','Colombiano':'Colombia','Colombiana':'Colombia',
    'Costa Rica':'Costa Rica','Costa Rican':'Costa Rica',
    'Cape Verde':'Cape Verde','Cape Verdean':'Cape Verde',
    'Czechia':'Czechia','Germany':'Germany','German':'Germany',
    'Dominica':'Dominica','Algeria':'Algeria','Algerian':'Algeria',
    'Ecuador':'Ecuador','Ecuadorian':'Ecuador',
    'Spain':'Spain','Spanish':'Spain',
    'Ethiopia':'Ethiopia','Ethiopian':'Ethiopia',
    'Finland':'Finland','Finnish':'Finland',
    'France':'France','French':'France',
    'United Kingdom':'United Kingdom','British':'United Kingdom',
    'Brit':'United Kingdom',
    'Ghana':'Ghana','Ghanian':'Ghana',
    'Gambia':'Gambia','Gambian':'Gambia',
    'Guinea':'Guinea','Greece':'Greece','Greek':'Greece',
    'Guatemala':'Guatemala','Guatemalan':'Guatemala',
    'Honduras':'Honduras','Honduran':'Honduras',
    'Croatia':'Croatia','Croatian':'Croatia',
    'Hungary':'Hungary','Hungarian':'Hungary',
    'Ireland':'Ireland','Irish':'Ireland',
    'Israel':'Israel','Israeli':'Israel',
    'India':'India','Indian':'India',
    'Iraq':'Iraq','Iraqi':'Iraq',
    'Iran':'Iran','Iranian':'Iran','Persian':'Iran',
    'Italy':'Italy','Italian':'Italy',
    'Jamaica':'Jamaica','Jamaican':'Jamaica',
    'Jordan':'Jordan','Jordanian':'Jordan',
    'Japan':'Japan','Japanese':'Japan',
    'Kenya':'Kenya','Kenyan':'Kenya',
    'Cambodia':'Cambodia','Cambodian':'Cambodia',
    'Lebanon':'Lebanon','Lebanese':'Lebanon',
    'Lithuania':'Lithuania','Lithuanian':'Lithuanian',
    'Libya':'Libya','Libyan':'Libya',
    'Morocco':'Morocco','Moroccan':'Morocco',
    'Monaco':'Monaco','Mali':'Mali',
    'Nicaragua':'Nicaragua',
    'Peru':'Peru','Peruvian':'Peru','Peruana':'Peru','Peruana':'Peru',
    'Philippines':'Philippines','Filipino':'Philippines','Filipina':'Philippines',
    'Pakistan':'Pakistan','Paki':'Pakistan','Pakistani':'Pakistan',
    'Poland':'Poland','Polish':'Poland',
    'Portugal':'Portugal','Portuguese':'Portugal',
    'Paraguay':'Paraguay','El Salvador':'El Salvadorian','Salvadorian':'El Salvador',
    'Turkey':'Turkey','Turkish':'Turkey',
    'England':'United Kingdom','English':'United Kingdom',
    'Ukraine':'Ukraine','Ukrainian':'Ukraine','Chingana':'Mexico',



    
}
    horo_map = {
    'Aries':'Aries',
    'aries':'Aries',
    'Taurus':'Taurus',
    'taurus':'Taurus',
    'Gemini':'Gemini',
    'gemini':'Gemini',
    'Cancer':'Cancer',
    'cancer':'Cancer',
    'Leo':'Leo',
    'leo':'Leo',
    'Virgo':'Virgo',
    'virgo':'Virgo',
    'Libra':'Libra',
    'libra':'Libra',
    'Scorpio':'Scorpio',
    'scorpio':'Scorpio',
    'Sagittarius':'Sagittarius',
    'sagittarius':'Sagittarius',
    'Capricorn':'Capricorn',
    'capricorn':'Capricorn',
    'Aquarius':'Aquarius',
    'aquarius':'Aquarius',
    'Pisces':'Pisces',
    'pisces':'Pisces'
}
    job_map = {
    'attorney':'Attorney','Attorney':'Attorney','DJ':'DJ','dj':'DJ',
    'streamer':'Streamer',
    'Influencer':'Influencer','influencer':'Influencer','INFLUENCER':'Influencer',
    'Artist':'Artist','artist':'Artist',
    'Mgmt':'Management','Management':'Management',
    'Teacher':'Teacher','teacher':'Teacher',
    'entrepreneur':'Entrepreneur','Entrepreneur':'Entrepreneur',
    'Screenwriter':'Screenwriter',
    'co-host':'co-host',
    'Director':'Director',
    'lawyering':'Attorney','Lawyer':'Attorney',
    'Realtor':'Real Estate','REALTOR':'Real Estate',
    'Founder':'Entrepreneur','founder':'Entrepreneur','Co-Founder':'Entrepreneur','co-founder':'Entrepreneur',
    'ENTREPRENEUR':'Entrepreneur',
    'author':'Author','Author':'Author',
    'columnist':'Columnist','Columnist':'Columnist',
    'Producer':'Producer','producer':'Producer',
    'architect':'Architect',
    'journalist':'Journalist','Journalist':'Journalist',
    'teacher':'Teacher','Teacher':'Teacher',
    'Economist':'Economist','economist':'Economist',
    'Contractor':'Contractor','contractor':'Contractor',
    'Host':'Host','host':'Host',
    'artist':'Artist','Artist':'Artist',
    'editor':'Editor','Editor':'Editor',
    'COO':'COO','CEO':'CEO',
    'educator':'Educator','Educator':'Educator',
    'writer':'Writer','Writer':'Writer',
    'content':'Content Creator','Content':'Content Creator','content creator':'Content Creator',
    'Designer':'Designer','designer':'Designer','Creative Director':'Creative Director','creative director':'Creative Director',
    'Psychology':'Psychology','CRYPTO TRADER':'Cryptocurrency',
    'IT Specialist':'Information Technology',
    'Comedian':'Comedian','comedian':'Comedian',
    'Music Producer':'Music Producer','music producer':'Music Producer',
    'Stylist':'Stylist','Fitness instructor':'Fitness Instructor',
    'Web Developer':'Developer','Developer':'Developer','Nail Artist':'Artist','Gamer':'Gamer',
    'Designer':'Designer','musician':'Musician','Musician':'Musician','model':'Model','Model':'Model',
    'Radio Personality':'Radio', 'Grammy artist':'Grammy Winner','life coach':'Life Coach',
    'Theater':'Theater','Theater Actor':'Theater', 'Performing Artist':'Artist','Exhibitionist':'Exhibitionist',
    'Digital Strategist':'Digital Strategist', 'Recording Artist':'Artist','Astronaut':'Astronaut','Voice Actor':'Actor',
    'Product Designer':'Product Designer','MUA':'Make Up Artist', 'Creator':'Creator','chef':'Chef','Chef':'Chef',
    'Blogger':'Blogger','Business Owner':'Entrepreneur','business owner':'Entrepreneur','Patron':'Patron',
    'Exec Director':'Executive Director','Executive Director':'Executive Director','digital creator':'Digital Creator','Digital Creator':'Digital Creator',
    'Brand Ambassador':'Brand Ambassador','brand ambassador':'Brand Ambassador','onlyfans':'Onlyfans','OnlyFans':'Onlyfans',
    'coach': 'Coach', 'Coach': 'Coach', 'Youtuber': 'Youtuber', 'youtuber': 'Youtuber','OF':'Onlyfans','songwriter':'Songwriter','Songwriter':'Songwriter',
    'ONLYFANS':'Onlyfans','Traveler':'Traveling','Traveling':'Traveling','Animator':'Animation', 'singer-songwriter':'Singer-Songwriter',
    'Fortnite':'Fortnie',



}
    major_map ={
    'Bioengineering':'Biological Engineering',
    'Systems Engineering':'Systems Engineering','Civil Engineering':'Civil Engineering',
    'Political Science':'Political Science', 'software engineering':'Computer Science',
    

    }
    edu_level_map = {
    'PhD':'PhD','Alumna':'Woman College Graduate','Ed.D':'Doctor in Education','MBA':'Masters in Business Administration',
    'mba':'Masters in Business Administration','Ph.D':'PhD',


        
    }
    college_map = {
    'RU':'Rutgers University','LSU':'Louisiana State University',
    'mizzou':'University of Missouri','Mizzou':'University of Missouri',
    'Haverford':'Haverford College','LSU Alumna':'Louisiana State University',
    'Texas A&M':'Texas A&M University','of Kentucky':'University of Kentucky',
    'SHSU Alumna':'Sam Houston State University','Alabama State':'Alabama State University',
    'Morgan State':'Morgan State University','LU Alum':'Lincoln University','Washington University':'Washingston University',
    'Arcadia University':'Arcadia University', 'University of Malta':'University of Malta',
    'OSU':'Ohio State University','Ohio State University':'Ohio State University'
    }
    interests_map = {
    'biking':'Biking','Biking':'Biking','cyclist':'Biking',
    'BLM':'Black Lives Matter','blm':'Black Lives Matter','#BlackLivesMatter':'Black Lives Matter','#BLACKLIVESMATTER':'Black Lives Matter',
    'Antiracist':'Anti Racist','Antisexist':'Anti Sexist',
    'nature':'Nature Lover',
    'photographer':'Photography','Photographer':'Photographer',
    'Stocks':'Stock Market','Forex':'FX Trading','Crypto':'Cryptocurrency',
    'activist':'Activist','Activist':'Activist',
    '#StopAsianHate':'Stop Asian Hate',
    'Veteran':'Veteran','Fashion':'Fashion','fashion':'Fashion',
    'Feminist':'Feminist','Anti-colourist':'Anti Racist',
    'Army':'United States Army','entertainment':'Entertainment','Entertainment':'Entertainment',
    'NFT':'NFT Enthusiast','#NFTArt':'NFT Ethusiast','Bestselling Author':'Bestselling Author',
    '#Bitcoin':'Bitcoin Enthusiast','Investor':'Investor',
    'Activist':'Activism', 'mental heath':'Mental Health',
    'BTS':'BTS Enthusiast','Pro Wrestler':'Wrestler','Motivational Speaker':'Motivational Speaker',
    'Gym Junkie':'Gym Enthusiast','Crypto Investor':'Cryptocurrency',
    'BLACK LIVES':'Black Lives Matter','Basketball player':'Basketball',
    '#Gamer':'Video Games','#Pc':'Video Games','crypto enthusiast':'Cryptocurrency',
    'Song Writer':'Song Writer','Vegan':'Vegan','Anime Fan':'Anime','Thespian':'Theater',
    'Singer':'Singer','Animal Lover':'Animals','animal lover':'animals','plant based':'Vegetarian', '18+':'Adult Content',
    'laughter':'Comedy','Comedy':'Comedy','#LOVEISLOVE':'LGBTQ+','#ALLY':'LGBTQ+','Pride Flag':'LGBTQ+','Rainbow Flag':'LGBTQ+',
    'NSFW':'Adult Content','Hunting':'Hunting','Fishing':'Fishing', 'Public Policy':'Public Policy','MUA':'Make Up Artist',
    'Yogi':'Yoga', 'blogger':'Blogger','Blogger':'Blogger','Beauty':'Beauty','Sustainability':'Sustainability','Cosplay':'Cosplay',
    'cosplay':'Cosplay','Games':'Video Games','heath':'Health','Health':'Health','beauty':'Beauty','Esthetician':'Esthetician','esthetician':'Esthetician',
    'PSN':'Video Games','psn':'Video Games','Counselling':'Mental Health','wellness':'Wellness','Wellness':'Wellness','skincare':'Skincare','Skincare':'Skincare',
    'cosplayer':'Cosplay','twitch':'Video Games', 'Twitch':'Video Games','fan account':'Fan Account','Fan Account':'Fan Account',
    'Skin Care':'Skin Care','Hair Care':'Hair Care','Podcast':'Podcast','podcast':'Podcast','Technology':'Technology','technology':'Technology',
    'Finance':'Finance','finance':'Finance','#skincare': 'Skin Care','vegan':'Vegan','Vegan':'Vegan','Political Junkie':'Political Science',
    'Boxing':'Boxing','MMA':'Mixed Martial Arts', 'screenwriter':'Screenwriter','Analyst':'Analyst','analyst':'Analyst',








    }
    family_map = {
    'Dad':'Dad','dad':'Dad','father':'Father','Father':'Father',
    'husband':'Husband','Mother':'Mother','#boymom':'Mother',
    'Mommy':'Mother','Wifey':'Wife','Wife':'Wife','wife':'Wife','mum':'Mother','Mum':'Mother',

    }
    
    sports_map = {
    '@mancity':'Manchester City',
    'ManU':'Manchester United',
    'Broncos':'Denver Broncos','broncos':'Denver Broncos',
    'colts':'Indianapolis Colts','Colts':'Indianapolis Colts',
    '#MambaMentality':'Kobe Fan','#TheMambaNeverDies':'Kobe Fan','Mamba Forever':'Kobe Fan',
    '#TarheelNation':'UNC Tarheels','#CowboysNation':'Dallas Cowboys',
    '#Lakeshow':'Los Angeles Lakers','Duke Basketball':'Duke University Basketball','#Celtics':'Boston Celtics',
    'Manchester United':'Manchester United','Arsenal FC':'Arsenal','Man city':'Manchester City',
    'Knicks':'New York Knicks','NY Knicks':'New York Knicks','Giants':'New York Giants','Yankees':'New York Yankees',
    }
    political_map = {
    '#Trump':'Trump','MAGA':'Trump','#MAGA':'Trump','#TrumpWon':'Trump',
    'democrat':'Democrat',
    'liberal':'Liberal',
    'Libertarian':'Libertarian','libertarian':'Libertarian','Conservative':'Conservative'
    }
    
    religious_map = {
    'Athiest':'Athiest','athiest':'Athiest',
    'God':'Believes in God', "Jesus is Lord":"Christian",
    'inshallah':'Muslim','Inshallah':'Muslim','Jesus':'Christian',
    'God First':'Christian','Latin Cross':'Christian','Allah':'Muslim','loves God':'Christian',
    'proverbs':'Christian','Proverbs':'Christian','Romans':'Christian','Love Jesus':'Christian','LOVE JESUS':'Christian',
        
    }
    
    martial_status={
    'single':'Single','Married':'Married','married':'Married','fiance':'Fiance','fiancé':'Fiance',
        
    }
    
    greek_map ={
    '1908':'Alpha Kappa Alpha','1914':'Phi Beta Sigma','ΑΦΑ':'Alpha Phi Alpha'
    }


    pronoun_map ={
     'he/him':'He/Him/His','He/Him/His':'He/Him/His','he/him/his':'He/Him/His','he/him':'He/Him/His'

    }
    return city_map,nat_map,horo_map,job_map,major_map,edu_level_map,college_map,interests_map,family_map,sports_map,political_map,religious_map,martial_status,greek_map

