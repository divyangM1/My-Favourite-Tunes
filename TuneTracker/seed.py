from .models import *
import random

# List of Indian classical musicians
indian_classical_musicians = [
    "Kishori Amonkar",
    "T. Balasaraswati",
    "Anil Biswas",
    "Nasir Aminuddin Dagar",
    "Shobha Gurtu",
    "Gangubai Hangal",
    "Bhimsen Joshi",
    "Kishore Kumar",
    "Lata Mangeshkar",
    "Muhammed Rafi",
    "Jagjit Singh",
    "Suraiya"
]

# List of International musicians
international_musicians = [
    "Aaliyah",
    "Roy Acuff",
    "Edie Adams",
    "Christina Aguilera",
    "Betty Allen",
    "Luther Allison",
    "Lucine Amara",
    "Carl Anderson",
    "Marian Anderson",
    "LaVerne Andrews",
    "Maxene Andrews",
    "Patty Andrews",
    "Paul Anka",
    "Charles Anthony",
    "Louis Armstrong",
    "Eddy Arnold",
    "Nick Ashford",
    "Gene Autry",
    "Frankie Avalon",
    "Hoyt Wayne Axton",
    "Erykah Badu",
    "Joan Baez",
    "Mildred Bailey",
    "Anita Baker",
    "Chet Baker",
    "Otis Blackwell",
    "James Blackwood",
    "Bobby ('Blue') Bland",
    "Mary J. Blige",
    "Sonny Bono",
    "Pat Boone",
    "The Boswell Sisters",
    "Boxcar Willie",
    "Laura Branigan",
    "Fanny Brice",
    "Garth Brooks",
    "Leon Eric ('Kix') Brooks",
    "Big Bill Broonzy",
    "Anne Wiggins Brown",
    "Charles Brown",
    "Chris Brown",
    "Gatemouth Brown",
    "James Brown"
]
# List of songs to add to database
songs_list = ['Sun Saathiya', 'Yesterday', 'Tum Hi Aana', 'I Want to Know What Love Is', 'Kabira',
          'Muskurane Ki Wajah Tum Ho', 'Mera Mann', 'Hotel California', 'Johnny B. Goode', 'The Girl from Ipanema', 
          'Brown Eyed Girl', 'Wish You Were Here', 'Kala Chashma', 'Tum Mile', 'High Rated Gabru', 'Tum Hi Ho',
         "Ain't No Mountain High Enough", "Don't Stop Believin'", 'Boogie Wonderland', 'Hallelujah', 'Kya Baat Ay', 
         'Chura Liya Hai Tumne Jo Dil Ko', 'Sicko Mode', 'Stand by Me', 'Saathiya', 'Imagine', 'Dancing Queen', 
         'Teri Khair Mangdi', 'Daru Badnaam', 'Gallan Goodiyaan', 'Jatt Da Blood', 'Despacito', 'Piya Basanti', 
         'Man in the Mirror', 'Breathless', "Sweet Child o' Mine", 'Fly Me to the Moon', 'Respect', 
         'Bille Bille Naina Waliye', 'Daaru Party', 'Sip Sip', 'Tere Bina Zindagi Se', 'Naina Da Kya Kasoor', 
         'Thriller', 'Smells Like Teen Spirit', 'Pee Pa Pee Pa', 'I Heard It Through the Grapevine', 'Sunflower', 
         'Dil Todeya', 'Koi Vi Nahi', "I Can't Help Myself (Sugar Pie Honey Bunch)", 'Kal Ho Naa Ho', 'Tera Ban Jaunga', 
         'Tum Jo Aaye', 'Yeh Jawaani Hai Deewani', 'American Pie', 'Lag Jaa Gale', 'Jiya Dhadak Dhadak Jaye', 
         "Blowin' in the Wind", 'Tere Naam', 'Stairway to Heaven', 'Jatt Ludhiyane Da', 'Drops of Jupiter', 'Crazy', 
         'Bridge Over Troubled Water', 'Georgia on My Mind', 'Hawayein', 'So High', 'Ae Dil Hai Mushkil', 'Channa Mereya', 
         'Mithi Mithi', 'I Want to Hold Your Hand', 'Hey Jude', 'Shape of You', 'Piano Man', 'Qismat', 'Pee Loon', 'Naah', 
         'Yaar Beli', 'Tears in Heaven', 'Wannabe', 'Koi Mil Gaya', 'Jai Ho', 'Blackbird', 'Illegal Weapon', 
         'Rolling in the Deep', 'I Will Always Love You', 'Jeene Laga Hoon', 'Pal Pal Dil Ke Paas', 'Mere Haath Mein', 
         'My Girl', 'Bom Diggy Diggy', 'Hauli Hauli', 'Gallan Mithiyan', 'Bairi Piya', 'Ae Mere Humsafar', 
         'Chookar mere man ko', 'Old Town Road', 'Like a Virgin', 'Main Tera Boyfriend', 'All You Need Is Love', 
         'Jatt Da Pajama', 'Every Breath You Take', 'Let It Be', 'Havana', 'Tera Ghata', 'Billie Jean', 'Janam Janam', 
         'I Will Survive', 'Bol Do Na Zara', 'Laung Laachi', 'Rocket Man', 'Lamberghini', 'Jatt Da Muqabala', 'Tere Bina', 
         'My Way', 'Unchained Melody', 'Mile Sur Mera Tumhara', 'Duniyaa', 'Do You Know', 'Suit Punjabi', 'Dil Chori', 
         'Laembadgini', 'Like a Rolling Stone', "What's Going On", "Ain't That a Kick in the Head", 'Gulabi Aankhen', 
         'Phir Le Aaya Dil', '3 Peg', 'Bapu Zimidar', 'Purple Haze', 'Raat Kamaal Hai', 'Superstition', 'Bad Guy', 
         'Hasi Ban Gaye', 'Jind Mahi', 'La Bamba', 'What a Fool Believes', 'Angie', 'Mere Rashke Qamar', 
         'Kajra Mohabbat Wala', 'Raatan', 'The Sound of Silence', "The Times They Are a-Changin'", 'Yeh Haseen Wadiyan', 
         'Gall Goriye', "Livin' on a Prayer", 'Sweet Caroline', 'Suit Suit', 'Proud Mary', 'Diljit Dosanjh', 'Nikle Currant', 
         'Pagal', 'Morni Banke', 'Yeh Jo Mohabbat Hai', 'Watermelon Sugar', 'Hornn Blow', 'Tum Se Hi', 'Coca Cola', 'Wonderwall', 
         'Leja Re', 'Ishq Da Uda Adaa', 'Take Me Home, Country Roads', 'Kaun Tujhe', 'Raabta', 'Gabru', 'Over the Rainbow', 
         'What a Wonderful World', 'Tera Hone Laga Hoon', 'Downtown', 'Uptown Funk', 'Sweet Home Alabama', 
         'Bad Romance', 'O Mere Dil Ke Chain', 'Agar Tum Saath Ho', 'Summertime', 'Teri Ore']

musicians = international_musicians + indian_classical_musicians

# Function to add Artists to the backend in bulk
def seed_db():
    
    for i in musicians:
        Artist.objects.create(name = i)


# Function to add songs with respect to Artists, used random as some artists can have multiple songs.
def song_name():
    artist_name = Artist.objects.all()
    for i in artist_name:
        random_iteration = random.randint(1,5)
        for j in range(random_iteration):
            if len(songs_list)>0:

                Song.objects.create(title=songs_list[0],artist=i)
                songs_list.pop(0)
            else:
                break

    print(songs_list)
