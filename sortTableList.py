def sortTableList(l,index):
    d = {}
    for row in l:
        d[row[index]] = row
    keyList = d.keys()
    for i in range(len(keyList)):
        
    

print sortTableList([['1', 'Wooly Bully ', 'Sam The Sham And The Pharaohs ', '1965', '125', '64'], ['2', 'I Cant Help Myself Sugar Pie Honey Bunch ', 'Four Tops ', '1965', '204', '94'], ['3', 'I Cant Get No Satisfaction ', 'The Rolling Stones ', '1965', 'No Lyrics Available', ''], ['4', 'You Were On My Mind ', 'We Five ', '1965', '152', '44'], ['5', 'Youve Lost That Lovin Feelin ', 'The Righteous Brothers ', '1965', '232', '88'], ['6', 'Downtown ', 'Petula Clark ', '1965', '239', '120'], ['7', 'Help ', 'The Beatles ', '1965', '228', '76'], ['8', 'Cant You Hear My Heart Beat ', 'Hermans Hermits ', '1965', '215', '72'], ['9', 'Crying In The Chapel ', 'Elvis Presley ', '1965', '148', '79'], ['10', 'My Girl ', 'The Temptations ', '1965', '153', '61'], ['11', 'Help Me Rhonda ', 'The Beach Boys ', '1965', '299', '65'], ['12', 'King Of The Road ', 'Roger Miller ', '1965', '169', '85'], ['13', 'The Birds And The Bees ', 'Jewel Akens ', '1965', '204', '57'], ['14', 'Hold Me Thrill Me Kiss Me ', 'Mel Carter ', '1965', '241', '73'], ['15', 'Shotgun ', 'Junior Walker The All Stars ', '1965', '134', '54'], ['16', 'I Got You Babe ', 'Sonny Cher ', '1965', '222', '94'], ['17', 'This Diamond Ring ', 'Gary Lewis The Playboys ', '1965', '170', '64'], ['18', 'The In Crowd ', 'Ramsey Lewis Trio ', '1965', '1', '1'], ['19', 'Mrs Brown Youve Got A Lovely Daughter ', 'Hermans Hermits ', '1965', '198', '85'], ['20', 'Stop In The Name Of Love ', 'The Supremes ', '1965', '233', '85']],1)
