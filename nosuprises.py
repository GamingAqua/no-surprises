import time

def print_lirik(bpm):
    beat = bpm / 60  # Calculate the duration of one beat
    # Adjust the delays based on the beat duration
    lirik = [
        ("", 25, 0.0),  # Extended intro pause
        ("A heart that's full up like a landfill, ", 2.5  * beat  , 0.1 * beat),
        ("A job that slowly kills you", 2.5  * beat, 0.1 * beat),
        ("Bruises that won't heal, ",  2.5  * beat ,  0.1 * beat ),
        ("", 4.9, 0.0),
        ("You look so tired, unhappy",  2.5  * beat ,  0.1 * beat ),
        ("Bring down the government, ",  2.5  * beat ,  0.1 * beat ),
        ("They don't, they don't speak for us",  2.5  * beat ,  0.1 * beat ),
        ("", 4.9, 0.0),
        ("I'll take a quiet life", 2.5  * beat ,  0.1 * beat ),
        ("A handshake of carbon monoxide", 2.5 * beat ,  0.1 * beat ),
        ("No alarms and no surprises",  2.5  * beat ,  0.1 * beat ),
        ("No alarms and no surprises",  2.5  * beat ,  0.1 * beat ),
        ("No alarms and no surprises", 2.5 * beat,  0.1 * beat ),
        
        ("Silent", 5 ,  0.1 * beat ), 
        ("Silent", 5 ,  0.1 * beat ),
        
        ("This is my final fit",  2.5  * beat ,  0.1 * beat ),
        ("My final bellyache with",  2.5  * beat ,  0.1 * beat ),
        
        ("No alarms and no surprises", 2.5  * beat ,  0.1 * beat ),
        ("No alarms and no surprises", 2.5  * beat ,  0.1 * beat ),
        ("No alarms and no surprises, please", 2.5 * beat ,  0.1 * beat ),
        ("", 20, 0.0),
        ("Such a pretty house", 2.5  * beat ,  0.1 * beat ),
        ("And such a pretty garden", 2.5  * beat ,  0.1 * beat ),
        
        ("No alarms and no surprises (get me out of here)", 2.5  * beat ,  0.1 * beat ),
        ("No alarms and no surprises (get me out of here)", 2.5  * beat ,  0.1 * beat ),
        ("No alarms and no surprises (get me out of here)", 2.5  * beat ,  0.1 * beat ),
        
            ("Please", 2.5  * beat ,  0.1 * beat )  # Final word lingers for impact
        ]

    for teks, delay_baris, delay_huruf in lirik:
        for c in teks:
            print(c, end='', flush=True)
            time.sleep(delay_huruf)
        print()  # Newline after each lyric line
        time.sleep(delay_baris)

if __name__ == "__main__":
    bpm = 70  # Set the BPM of the song
    print("\n\n\n\n")
    print_lirik(bpm)
    