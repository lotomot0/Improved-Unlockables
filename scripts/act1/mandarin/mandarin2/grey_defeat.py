# Generated by BehavEd, Made compatible with Outsider's EXG mod
# ( "Grey Gargoyle defeated!" )
waittimed ( 0.100 )
unlockCharacter("colossus", "" )
waittimed ( 0.100 )
unlockCharacter("mdr", "" )
waittimed ( 0.100 )
unlockCharacter("shokpl", "" )
waittimed ( 0.100 )
unlockCharacter("SG", "" )
waittimed ( 0.100 )
unlockCharacter("Shroud", "" )
waittimed ( 0.100 )
unlockCharacter("Siryn", "" )
waittimed ( 0.100 )
unlockCharacter("moonstone", "" )
waittimed ( 0.100 )
unlockCharacter("morph", "" )
waittimed ( 0.100 )
unlockCharacter("pat", "" )
waittimed ( 0.100 )
unlockCharacter("spd", "" )
waittimed ( 0.100 )
setDefaultTarget("" )
setMusicOverride("", 1.000 )
setGameFlag("bosses", 10, 1 )
objective ( "mandarin_obj30",  "EOBJCMD_COMPLETE" )
waittimed ( 0.100 )
sound (  "PLAY_SOUND", "common/game/achievement", "", "" )
createPopupDialogXml("dialogs/special/greygargoyle_achievement" )
waittimed ( 0.100 )
awardReputation("", 50 )
awardAchievement("", "defeated_greygargoyle" )
startConversation("act1/mandarin/mandarin2/1_mandarin2_035" )

