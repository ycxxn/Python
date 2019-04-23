from TV import TV 

def main():
    tv1=TV()
    tv1.turnOn()
    tv1.setChannel(30)
    tv1.setVolume(3)

    tv2=TV()
    tv2.turnOn()
    tv2.channelUp()
    tv2.channelUp()
    tv2.volumeUp()

    print("tv1頻道",tv1.getChannel(),"音量",tv1.getVolume())
    print("tv2頻道",tv2.getChannel(),"音量",tv2.getVolume())

if __name__ == "__main__":
    main()
    

