import mido
import numpy as np
import sys
import random
import xlwt
np.set_printoptions(threshold=sys.maxsize) #set full output
path =["archive/albeniz/alb_esp1.mid", "archive/albeniz/alb_esp2.mid", "archive/albeniz/alb_esp3.mid", "archive/albeniz/alb_esp4.mid", "archive/albeniz/alb_esp5.mid", "archive/albeniz/alb_esp6.mid","archive/albeniz/alb_se1.mid", "archive/albeniz/alb_se2.mid", "archive/albeniz/alb_se3.mid", "archive/albeniz/alb_se4.mid", "archive/albeniz/alb_se5.mid", "archive/albeniz/alb_se6.mid", "archive/albeniz/alb_se7.mid", "archive/albeniz/alb_se8.mid","archive/bach/bach_846.mid", "archive/bach/bach_847.mid", "archive/bach/bach_850.mid","archive/balakir/islamei.mid","archive/beeth/appass_1.mid", "archive/beeth/appass_2.mid", "archive/beeth/appass_3.mid","archive/beeth/beethoven_hammerklavier_1.mid", "archive/beeth/beethoven_hammerklavier_2.mid", "archive/beeth/beethoven_hammerklavier_3.mid", "archive/beeth/beethoven_hammerklavier_4.mid","archive/beeth/beethoven_les_adieux_1.mid", "archive/beeth/beethoven_les_adieux_2.mid", "archive/beeth/beethoven_les_adieux_3.mid","archive/beeth/beethoven_opus10_1.mid", "archive/beeth/beethoven_opus10_2.mid", "archive/beeth/beethoven_opus10_3.mid","archive/beeth/beethoven_opus22_1.mid", "archive/beeth/beethoven_opus22_2.mid", "archive/beeth/beethoven_opus22_3.mid", "archive/beeth/beethoven_opus22_4.mid","archive/beeth/beethoven_opus90_1.mid", "archive/beeth/beethoven_opus90_2.mid","archive/beeth/elise.mid","archive/beeth/mond_1.mid", "archive/beeth/mond_2.mid", "archive/beeth/mond_3.mid","archive/beeth/pathetique_1.mid", "archive/beeth/pathetique_2.mid", "archive/beeth/pathetique_3.mid","archive/beeth/waldstein_1.mid", "archive/beeth/waldstein_2.mid", "archive/beeth/waldstein_3.mid","archive/borodin/bor_ps1.mid", "archive/borodin/bor_ps2.mid", "archive/borodin/bor_ps3.mid", "archive/borodin/bor_ps4.mid", "archive/borodin/bor_ps5.mid", "archive/borodin/bor_ps6.mid", "archive/borodin/bor_ps7.mid","archive/brahms/br_im2.mid", "archive/brahms/br_im5.mid", "archive/brahms/BR_IM6.mid", "archive/brahms/br_rhap.mid", "archive/brahms/brahms_opus1_1.mid", "archive/brahms/brahms_opus1_2.mid", "archive/brahms/brahms_opus1_3.mid", "archive/brahms/brahms_opus1_4.mid", "archive/brahms/brahms_opus117_1.mid", "archive/brahms/brahms_opus117_2.mid","archive/burgm/burg_agitato.mid", "archive/burgm/burg_erwachen.mid", "archive/burgm/burg_geschwindigkeit.mid", "archive/burgm/burg_gewitter.mid", "archive/burgm/burg_perlen.mid", "archive/burgm/burg_quelle.mid", "archive/burgm/burg_spinnerlied.mid", "archive/burgm/burg_sylphen.mid", "archive/burgm/burg_trennung.mid","archive/chopin/chp_op18.mid", "archive/chopin/chp_op31.mid", "archive/chopin/chpn_op7_1.mid", "archive/chopin/chpn_op7_2.mid", "archive/chopin/chpn_op10_e01.mid", "archive/chopin/chpn_op10_e05.mid", "archive/chopin/chpn_op10_e12.mid", "archive/chopin/chpn_op23.mid", "archive/chopin/chpn_op25_e1.mid", "archive/chopin/chpn_op25_e2.mid", "archive/chopin/chpn_op25_e3.mid", "archive/chopin/chpn_op25_e4.mid", "archive/chopin/chpn_op25_e11.mid", "archive/chopin/chpn_op25_e12.mid", "archive/chopin/chpn_op27_1.mid", "archive/chopin/chpn_op27_2.mid", "archive/chopin/chpn_op33_2.mid", "archive/chopin/chpn_op33_4.mid", "archive/chopin/chpn_op35_1.mid", "archive/chopin/chpn_op35_2.mid", "archive/chopin/chpn_op35_3.mid", "archive/chopin/chpn_op35_4.mid", "archive/chopin/chpn_op53.mid", "archive/chopin/chpn_op66.mid", "archive/chopin/chpn-p1.mid", "archive/chopin/chpn-p2.mid", "archive/chopin/chpn-p3.mid", "archive/chopin/chpn-p4.mid", "archive/chopin/chpn-p5.mid", "archive/chopin/chpn-p6.mid", "archive/chopin/chpn-p7.mid", "archive/chopin/chpn-p8.mid", "archive/chopin/chpn-p9.mid", "archive/chopin/chpn-p10.mid", "archive/chopin/chpn-p11.mid", "archive/chopin/chpn-p12.mid", "archive/chopin/chpn-p13.mid", "archive/chopin/chpn-p14.mid", "archive/chopin/chpn-p15.mid", "archive/chopin/chpn-p16.mid", "archive/chopin/chpn-p17.mid", "archive/chopin/chpn-p18.mid", "archive/chopin/chpn-p19.mid", "archive/chopin/chpn-p20.mid", "archive/chopin/chpn-p21.mid", "archive/chopin/chpn-p22.mid", "archive/chopin/chpn-p23.mid", "archive/chopin/chpn-p24.mid","archive/debussy/DEB_CLAI.mid", "archive/debussy/deb_menu.mid", "archive/debussy/DEB_PASS.mid", "archive/debussy/deb_prel.mid", "archive/debussy/debussy_cc_1.mid", "archive/debussy/debussy_cc_2.mid", "archive/debussy/debussy_cc_3.mid", "archive/debussy/debussy_cc_4.mid", "archive/debussy/debussy_cc_6.mid","archive/granados/gra_esp_2.mid", "archive/granados/gra_esp_3.mid", "archive/granados/gra_esp_4.mid","archive/grieg/grieg_album.mid", "archive/grieg/grieg_berceuse.mid", "archive/grieg/grieg_brooklet.mid", "archive/grieg/grieg_butterfly.mid", "archive/grieg/grieg_elfentanz.mid", "archive/grieg/grieg_halling.mid", "archive/grieg/grieg_kobold.mid", "archive/grieg/grieg_march.mid", "archive/grieg/grieg_once_upon_a_time.mid", "archive/grieg/grieg_spring.mid", "archive/grieg/grieg_voeglein.mid", "archive/grieg/grieg_waechter.mid", "archive/grieg/grieg_walzer.mid", "archive/grieg/grieg_wanderer.mid", "archive/grieg/grieg_wedding.mid", "archive/grieg/grieg_zwerge.mid","archive/haydn/hay_40_1.mid", "archive/haydn/hay_40_2.mid","archive/haydn/haydn_7_1.mid", "archive/haydn/haydn_7_2.mid", "archive/haydn/haydn_7_3.mid","archive/haydn/haydn_8_1.mid", "archive/haydn/haydn_8_2.mid", "archive/haydn/haydn_8_3.mid", "archive/haydn/haydn_8_4.mid","archive/haydn/haydn_9_1.mid", "archive/haydn/haydn_9_2.mid", "archive/haydn/haydn_9_3.mid","archive/haydn/haydn_33_1.mid", "archive/haydn/haydn_33_2.mid", "archive/haydn/haydn_33_3.mid","archive/haydn/haydn_35_1.mid", "archive/haydn/haydn_35_2.mid", "archive/haydn/haydn_35_3.mid","archive/haydn/haydn_43_1.mid", "archive/haydn/haydn_43_2.mid", "archive/haydn/haydn_43_3.mid","archive/liszt/liz_donjuan.mid", "archive/liszt/liz_et_trans4.mid", "archive/liszt/liz_et_trans5.mid", "archive/liszt/liz_et_trans8.mid", "archive/liszt/liz_et1.mid", "archive/liszt/liz_et2.mid", "archive/liszt/liz_et3.mid", "archive/liszt/liz_et4.mid", "archive/liszt/liz_et5.mid", "archive/liszt/liz_et6.mid", "archive/liszt/liz_liebestraum.mid", "archive/liszt/liz_rhap02.mid", "archive/liszt/liz_rhap09.mid", "archive/liszt/liz_rhap10.mid", "archive/liszt/liz_rhap12.mid", "archive/liszt/liz_rhap15.mid","archive/mendelssohn/mendel_op19_1.mid", "archive/mendelssohn/mendel_op19_2.mid", "archive/mendelssohn/mendel_op19_3.mid", "archive/mendelssohn/mendel_op19_4.mid", "archive/mendelssohn/mendel_op19_5.mid", "archive/mendelssohn/mendel_op19_6.mid", "archive/mendelssohn/mendel_op30_1.mid", "archive/mendelssohn/mendel_op30_2.mid", "archive/mendelssohn/mendel_op30_3.mid", "archive/mendelssohn/mendel_op30_4.mid", "archive/mendelssohn/mendel_op30_5.mid", "archive/mendelssohn/mendel_op53_5.mid", "archive/mendelssohn/mendel_op62_3.mid", "archive/mendelssohn/mendel_op62_4.mid", "archive/mendelssohn/mendel_op62_5.mid","archive/mozart/mz_311_1.mid", "archive/mozart/mz_311_2.mid", "archive/mozart/mz_311_3.mid", "archive/mozart/mz_330_1.mid", "archive/mozart/mz_330_2.mid", "archive/mozart/mz_330_3.mid", "archive/mozart/mz_331_1.mid", "archive/mozart/mz_331_2.mid", "archive/mozart/mz_331_3.mid", "archive/mozart/mz_332_1.mid", "archive/mozart/mz_332_2.mid", "archive/mozart/mz_332_3.mid", "archive/mozart/mz_333_1.mid", "archive/mozart/mz_333_2.mid", "archive/mozart/mz_333_3.mid", "archive/mozart/mz_545_1.mid", "archive/mozart/mz_545_2.mid", "archive/mozart/mz_545_3.mid", "archive/mozart/mz_570_1.mid", "archive/mozart/mz_570_2.mid", "archive/mozart/mz_570_3.mid","archive/muss/muss_1.mid", "archive/muss/muss_2.mid", "archive/muss/muss_3.mid", "archive/muss/muss_4.mid", "archive/muss/muss_5.mid", "archive/muss/muss_6.mid", "archive/muss/muss_7.mid", "archive/muss/muss_8.mid","archive/schubert/schu_143_1.mid", "archive/schubert/schu_143_2.mid", "archive/schubert/schu_143_3.mid", "archive/schubert/schub_d760_1.mid", "archive/schubert/schub_d760_2.mid", "archive/schubert/schub_d760_3.mid", "archive/schubert/schub_d760_4.mid", "archive/schubert/schub_d960_1.mid", "archive/schubert/schub_d960_2.mid", "archive/schubert/schub_d960_3.mid", "archive/schubert/schub_d960_4.mid", "archive/schubert/schubert_D850_1.mid", "archive/schubert/schubert_D850_2.mid", "archive/schubert/schubert_D850_3.mid", "archive/schubert/schubert_D850_4.mid", "archive/schubert/schubert_D935_1.mid", "archive/schubert/schubert_D935_2.mid", "archive/schubert/schubert_D935_3.mid", "archive/schubert/schubert_D935_4.mid", "archive/schubert/schuim-1.mid", "archive/schubert/schuim-2.mid", "archive/schubert/schuim-3.mid", "archive/schubert/schuim-4.mid", "archive/schubert/schumm-1.mid", "archive/schubert/schumm-2.mid", "archive/schubert/schumm-3.mid", "archive/schubert/schumm-4.mid", "archive/schubert/schumm-5.mid", "archive/schubert/schumm-6.mid","archive/schumann/schum_abegg.mid", "archive/schumann/scn15_1.mid", "archive/schumann/scn15_2.mid", "archive/schumann/scn15_3.mid", "archive/schumann/scn15_4.mid", "archive/schumann/scn15_5.mid", "archive/schumann/scn15_6.mid", "archive/schumann/scn15_7.mid", "archive/schumann/scn15_8.mid", "archive/schumann/scn15_9.mid", "archive/schumann/scn15_10.mid", "archive/schumann/scn15_11.mid", "archive/schumann/scn15_12.mid", "archive/schumann/scn15_13.mid", "archive/schumann/scn16_1.mid", "archive/schumann/scn16_2.mid", "archive/schumann/scn16_3.mid", "archive/schumann/scn16_4.mid", "archive/schumann/scn16_5.mid", "archive/schumann/scn16_6.mid", "archive/schumann/scn16_7.mid", "archive/schumann/scn16_8.mid", "archive/schumann/scn68_10.mid", "archive/schumann/scn68_12.mid","archive/tschai/ty_april.mid", "archive/tschai/ty_august.mid", "archive/tschai/ty_dezember.mid", "archive/tschai/ty_februar.mid", "archive/tschai/ty_januar.mid", "archive/tschai/ty_juli.mid", "archive/tschai/ty_juni.mid", "archive/tschai/ty_maerz.mid", "archive/tschai/ty_mai.mid", "archive/tschai/ty_november.mid", "archive/tschai/ty_oktober.mid", "archive/tschai/ty_september.mid"]
path =["pathetique_3.mid"]
note2 = np.zeros((2304,48)).astype(int) #second markov chain
NOTE_NAMES = {0:"C", 1:"C#", 2:"D", 3:"D#", 4:"E", 5:"F", 6:"F#", 7:"G", 8:"G#", 9:"A", 10:"A#", 11:"B"}
result =[]
#add note from midi to list
for j in range(len(path)):
    mid = mido.MidiFile(path[j])
    quatergrid=mid.ticks_per_beat/4
    note = [] #note in 1 midi files
    print(mid)
    for i, track in enumerate(mid.tracks):
#        print('Track {}: {}'.format(i, track.name))
        for msg in track:
            if msg.type=='note_on' or msg.type=='note_off':
                print(msg)
                time=int(np.ceil(msg.time/quatergrid))
                if time!=0:
                    if time>4:
                        time = 4
                    note.append(((msg.note%12)*4+time)-1)
    print(note)
    #add note to second markov chain
for i in range(len(note)-2):
    prevNote2=note[i]
    prevNote1=note[i+1]
    currentNote=note[i+2]
    note2[prevNote2 * 48 + prevNote1][currentNote] += 1

#output second markov chain
wb = xlwt.Workbook()
ws = wb.add_sheet('second markov')
for i in range(2304):
    temp=''
    temp=temp+str(NOTE_NAMES[np.floor(i/192)])
    temp=temp+str(int(np.floor(i/48)%4+1))
    temp=temp+str(NOTE_NAMES[np.floor((i/4)%12)])
    temp=temp+str((i%4)+1)
    ws.write(i+1,0,temp)
for j in range(48):
    temp=''
    temp=temp+str(NOTE_NAMES[np.floor(j/4)])
    temp=temp+str((j%4)+1)
    ws.write(0,j+1,temp)
for i in range(2304):
    for j in range(48):
        print(note2[i][j],end=" ")
        ws.write(i+1, j+1, int(note2[i][j]))
    print("")
wb.save('second markov.xls')

#output song
result.append(0)
result.append(8)
for i in range(100):
    prevNote2=result[i]
    prevNote1=result[i+1]
    randomtemp=0
    for j in range(48):
        randomtemp+=note2[prevNote2*48+prevNote1][j]
    randomtemp=randomtemp*random.random()
    for j in range(48):
        if randomtemp-note2[prevNote2*48+prevNote1][j]<0 :
            break
        randomtemp=randomtemp-note2[prevNote2*48+prevNote1][j]
    result.append(j)
for i in range(len(result)):
    noteresult=int(np.floor(result[i]/4))
    timeresult=(result[i]%4)+1
    print(NOTE_NAMES[noteresult],end="")
    print(timeresult)
    