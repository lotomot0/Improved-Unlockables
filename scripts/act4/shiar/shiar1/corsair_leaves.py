# Generated by BehavEd
# ( "Corsair has left" )
waittimed ( 0.100 )
unlockCharacter("corsairdlc", "" )
setGameFlag("shiar1", 10, 1 )
startCutScene("TRUE", "FALSE" )
waittimed ( 0.750 )
cameraMove(" 192.700 -1577.880 -195.580 ", 0.000 )
cameraPan(" 0.000 24.200 289.100 ", 0.000, "FALSE" )
moveHeroesToEnt("corsair_leaving" )
copyOriginAndAngles("corsair", "corsair_leaving01" )
waittimed ( 0.100 )
beATeamPlayer("corsair", "FALSE" )
cameraFade(0.000, 1.000 )
waittimed ( 1.000 )
startConversation("act4/shiar/shiar1/4_shiar1_030" )

