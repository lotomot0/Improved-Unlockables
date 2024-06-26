# Generated by BehavEd
# ( "turn off pitfall stuff" )
act("gators01", "gators01" )
act("gators02", "gators02" )
act("gators03", "gators03" )
act("pit_trap01", "pit_trap01" )
act("pit_trap02", "pit_trap02" )
# ( "is this the first time pitfall has been beaten?" )
check_pitfall = getGameFlag("murder2", 4 )
if check_pitfall == 0
     # ( "prepare zone exits" )
     actSilent("door_murder3", "door_murder3" )
     actSilent("door_murder4", "door_murder4" )
     setEnable("link_murder3", "TRUE" )
     setEnable("link_murder4", "TRUE" )
     # ( "this is the first pitfall win--use the jean grey ending" )
     setGameFlag("murder2", 4, 1 )
     startCutScene("FALSE", "FALSE" )
     cameraFade(1.000, 1.000 )
     waittimed ( 1.000 )
     setSpecialMode("" )
     setCharSwitchingOn("TRUE" )
     setAmbientLightColor(" 0.020 0.039 0.000 ", 0.100 )
     moveHeroesToEnt("hero_spot_tent" )
     setEnable("phoenix_npc", "TRUE" )
     act("phoenix_npc", "phoenix_npc" )
     waittimed ( 0.100 )
     playanim (  "EA_ZONE1", "jean", "LOOP", "" )
     cameraFocusToEntity("jean_place01", 416.000, 45.000, 165.000, 0.000 )
     cameraFOV(60.000, 0.000 )
     waittimed ( 0.750 )
     setMusicOverride("", 2.000 )
     cameraFocusToEntity("jean_place01", 288.000, 30.000, 150.000, 2.000 )
     cameraFade(0.000, 1.000 )
     waittimed ( 1.000 )
     playanim (  "EA_ZONE2", "jean", "NONE", "getup" )
     waitsignal ( "getup" )
     cyclops = isActorOnTeam("Cyclops" )
     nightcrawler = isActorOnTeam("Nightcrawlerdlc" )
     magneto = isActorOnTeam("Magneto" )
     if cyclops == 1
          waittimed ( 0.100 )
          sound (  "PLAY_SOUND", "common/game/achievement", "", "" )
          createPopupDialogXml("dialogs/special/cyclops_talk_achievement" )
          waittimed ( 0.100 )
          startConversation("act2/murder/murder2/2_murder2_072_dlc" )
     elif nightcrawler == 1
          startConversation("act2/murder/murder2/2_murder2_072_nc_dlc" )
     elif magneto == 1
          startConversation("act2/murder/murder2/2_murder2_070m" )
     else
          startCharConversation("act2/murder/murder2/2_murder2_070", "wolverine", "act2/murder/murder2/2_murder2_072" )
     endif
else
     # ( "pitfall has been beaten before--use the ending without jean grey" )
     startCutScene("FALSE", "FALSE" )
     cameraFade(1.000, 1.000 )
     waittimed ( 1.000 )
     setSpecialMode("" )
     setCharSwitchingOn("TRUE" )
     setAmbientLightColor(" 0.020 0.039 0.000 ", 0.100 )
     moveHeroesToEnt("hero_spot_tent" )
     setMusicOverride("", 2.000 )
     setRecallActive("TRUE" )
     cameraReset( )
     cameraFOV(60.000, 0.000 )
     cameraFade(0.000, 1.000 )
     waittimed ( 1.000 )
     endCutScene("FALSE", "TRUE" )
endif

