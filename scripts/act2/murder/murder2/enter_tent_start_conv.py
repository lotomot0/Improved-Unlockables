# Generated by BehavEd
# ( "comment" )
check = getGameFlag("murder2", 3 )
if check == 0
     startCutScene("FALSE", "FALSE" )
     cameraFade(1.000, 1.000 )
     waittimed ( 1.000 )
     moveHeroesToEnt("hero_spot_tent" )
     act("phoenix_npc", "phoenix_npc" )
     cameraFocusToEntity("jean_place01", 384.000, 45.000, 150.000, 0.000 )
     waittimed ( 0.750 )
     cameraFocusToEntity("jean_place01", 288.000, 30.000, 135.000, 2.000 )
     cameraFade(0.000, 1.000 )
     waittimed ( 0.750 )
     cyclops = isActorOnTeam("Cyclops" )
     if cyclops == 1
          waittimed ( 0.100 )
          sound (  "PLAY_SOUND", "common/game/achievement", "", "" )
          createPopupDialogXml("dialogs/special/cyclops_talk_achievement" )
          waittimed ( 0.100 )
     	  startConversation("act2/murder/murder2/2_murder2_014_dlc" )
     else
          startCharConversation("act2/murder/murder2/2_murder2_020", "invisiblewoman", "act2/murder/murder2/2_murder2_022" )
     endif
else
     # ( "does the player have the coin--should clowns come in?" )
     check_coin = getGameFlag("murder2", 7 )
     if check_coin == 0
          # ( "coin hasn't been picked up--is clown assault in progress?" )
          check_prog = getGameFlag("murder2", 9 )
          if check_prog == 0
               # ( "no--initiate clown assault" )
               setGameFlag("murder2", 9, 1 )
               startCutScene("FALSE", "FALSE" )
               cameraFade(1.000, 1.000 )
               waittimed ( 1.000 )
               moveHeroesToEnt("hero_spot_tent" )
               waittimed ( 0.100 )
               cameraFade(0.000, 0.250 )
               act("clown_face", "clown_face" )
               act("clown_car_go", "clown_car_go" )
               sound (  "PLAY_SOUND", "zone_shared/murderworld/clown_car_stream", "", "" )
               cameraFollowMotionPath("murder/clown_car_cam", "mp_clown_car_cam", "TRUE", "TRUE", "FALSE", "carstop" )
               waitsignal ( "carstop" )
               act("clown_face", "clown_face" )
               copyOriginAndAngles("clown_car_stop", "car_spot01" )
               remove ( "clown_car_go", "clown_car_go" )
               waittimed ( 0.100 )
               act("clown_car_stop", "clown_car_stop" )
               waittimed ( 0.100 )
               act("s_introclown", "s_introclown" )
               waittimed ( 2.000 )
               act("s_introclown", "s_introclown" )
               waittimed ( 2.000 )
               act("s_introclown", "s_introclown" )
               waittimed ( 2.500 )
               act("s_introleader", "s_introleader" )
               waittimed ( 3.750 )
               act("clown_car_stop", "clown_car_stop" )
               cameraReset( )
               cameraFOV(60.000, 0.000 )
               endCutScene("FALSE", "TRUE" )
               faceEntity("introclown", "_ACTIVE_HERO_" )
               faceEntity("introleader", "_ACTIVE_HERO_" )
               attackEntityWithType("introclown", "_ACTIVE_HERO_", "ANY", "FALSE" )
               attackEntityWithType("introleader", "_ACTIVE_HERO_", "ANY", "FALSE" )
          else
               lockControls(-1.000 )
               cameraFade(1.000, 1.000 )
               waittimed ( 1.000 )
               moveHeroesToEnt("hero_spot_tent" )
               waittimed ( 0.750 )
               cameraFade(0.000, 1.000 )
               lockControls(0.100 )
          endif
     else
          lockControls(-1.000 )
          cameraFade(1.000, 1.000 )
          waittimed ( 1.000 )
          moveHeroesToEnt("hero_spot_tent" )
          waittimed ( 0.750 )
          cameraFade(0.000, 1.000 )
          lockControls(0.100 )
     endif
endif

