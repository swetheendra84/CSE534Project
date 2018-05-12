import os
import sys
import subprocess

website_string = "zimbra.free.fr golfchannel.com 8muses.com javfor.me tiu.ru vppgamingnetwork.com dikaiologitika.gr trademe.co.nz sky.it mtggoldfish.com amarujala.com ae.com mysmartprice.com derstandard.at baseball-reference.com priceminister.com litres.ru money.pl fairwhale.tmall.com careers360.com check24.de evolife.cn todoist.com wmtransfer.com kaspersky.com gradeup.co curiouscat.me yle.fi alphashoppers.co zalando.de hochi.co.jp waploaded.com stuff.co.nz monsterindia.com starbucks.com anysex.com to8to.com honeys.tmall.com qcloud.com indiewire.com google.co.mz crazygames.com yoox.com puu.sh utah.edu mehrnews.com akairan.com pussysaga.com eatthis.com duga.jp instiz.net ticketmonster.co.kr mangapanda.com lazada.vn onclickmega.com tripadvisor.fr iha.com.tr delfi.lv tureng.com time.ir coinx.ph deadline.com nicehash.com mmaaxx.com newsru.com skyscrapercity.com imis.tmall.com myscore.com.ua theconversation.com ing.nl santandernet.com.br uloz.to bitflyer.jp ucsb.edu tweakers.net thinkprogress.org 36kr.com dhs.gov cian.ru bc.vc immobiliare.it definicion.de 7days.ru kotobank.jp yummyanime.com justwatch.com herphemiste.com aoredi.com opendns.com allmusic.com forocoches.com dawnnews.tv cuon.io shahrekhabar.com putlockers.tf buy123.com.tw xiami.com enotes.com eroprofile.com uproxx.com myreadingmanga.info 2ch.hk telugu360.com putlockertv.to wyborcza.pl etoro.com service-public.fr msnbc.com antpedia.com haa66855mo.club getresponse.com sony.com pixiv.net hbr.org libertyvf.net colourpop.com oantagonista.com 23andme.com giantbomb.com ntdtv.com holloporn.com zdnet.com yyets.com sarayanews.com ihg.com unsw.edu.au google.co.bw egitimhane.com rackspace.com hilltopads.net yinxiang.com mango.com thenewslens.com heureka.cz fontspace.com delfi.lt hamusoku.com mediatabtv.online moradu.com uwaterloo.ca readcomiconline.to lafuma.tmall.com graphicriver.net everychina.com jandan.net himasoku.com fiuxy.me rikunabi.com yahoo.com.tw ncore.cc answers.com hanime.tv cimbclicks.com.my iltalehti.fi evite.com arga-mag.com jezebel.com dict.cn topshop.tmall.com enstage-sas.com tp-link.com nu.nl saraiva.com.br fudan.edu.cn ovh.com moviescounter.co nbc.com lankasri.com tvmuse.com torrentfreak.com on.cc excite.co.jp pipedrive.com clicknupload.org mercadolibre.cl tabmemfree.appspot.com vov.vn baby.tmall.com animenewsnetwork.com redirectvoluum.com ih5.cn bouyguestelecom.fr bluewin.ch content.tmall.com read01.com angonoticias.com letscorp.net sammobile.com syf.com hackstore.net camwhores.tv anidub.com purple6401.com vulcan.net.pl rarbgmirror.org world.tmall.com torrentmovies.co tradebay.com acceder.gratis jang.com.pk my.com zhibo8.cc gdeposylka.ru pensador.com letterboxd.com vix.com collabserv.com rateyourmusic.com pdfdrive.net ngacn.cc gamme.com.tw vipergirls.to acesso.gov.pt poiskm.co echoroukonline.com arbeitsagentur.de fritz.box jawapos.com zoominfo.com pptv.com webmoney.ru nuomi.com is.fi vagaro.com ku.tmall.com tutu.ru eltiempo.com rule34.xxx slrclub.com boxofficemojo.com netvasco.com.br to10.gr fresherslive.com manga-zip.net bestbuy.ca 90tv.ir media-bucket.com pornktube.com freedownloadmanager.org dyson.tmall.com traveloka.com gsu.edu sport24.gr bazos.sk profit-opportunity.com russianfood.com coinpot.co iop.org skyscanner.com freenet.de taroot-rangi.com tparser.org nudevista.com bet365.es torrenthaja.com raspberrypi.org pornosveta.com ftchinese.com userbenchmark.com cas.sk edmunds.com c-sharpcorner.com producthunt.com ss.com cumlouder.com redsys.es wed114.cn www.nhs.uk blic.rs vietnamnet.vn overleaf.com pornhubpremium.com machieved.com ulta.com bigmir.net samehadaku.tv translit.net indiatoday.in education.com telecharger-youtube-mp3.com git-scm.com shatel.ir"

websites = website_string.split(' ')

#websites = ['www.google.com','www.facebook.com']
def main():
    hping_command = "sudo hping3 -S -V -c 25 -p 80 -i u100 {}"
    traceroute_command = "sudo tcptraceroute -m 50 {} {}"
    hping_file = open("hping.out",'a+')
    traceroute_file = open("traceroute.out",'a+')
    #website_file = open("websites.csv",'r')
    for website in websites:
	website=website.strip('\n')
	website=website.lstrip(' ')
	website=website.rstrip(' ')
        command = hping_command.format(website)
        print website
        hping_file.write("***"+website+"***"+"\n")
        hping_file.write("***"+command+"***"+"\n")
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            hping_file.write(line)
        retval = p.wait()
        hping_file.write("Return Code: "+str(retval))
        sys.stdout.flush()
        
        command = traceroute_command.format(website,80)
        traceroute_file.write("***"+command+"***"+"\n")
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            traceroute_file.write(line)
        retval = p.wait()
        traceroute_file.write("Return Code: "+str(retval))
        sys.stdout.flush()
        traceroute_file.write("\n\n")
    hping_file.close()
    traceroute_file.close()
        
        
main()
