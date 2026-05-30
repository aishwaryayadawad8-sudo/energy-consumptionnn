#!/usr/bin/env python3
"""
Enhanced Search with Country Suggestions and Location Pins
=========================================================

This script enhances the search functionality to:
1. Show country suggestions as you type in the search bar
2. Highlight selected countries with location pins/markers
3. Provide instant visual feedback like in the screenshot
"""

import os

def enhance_search_functionality():
    """Enhance search with suggestions and location pins"""
    
    html_file_path = "Aish/sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🔍 ENHANCING SEARCH WITH SUGGESTIONS AND LOCATION PINS")
    print("=" * 60)
    print(f"📁 Updating file: {html_file_path}")
    
    # Enhanced dashboard with improved search and location pins
    enhanced_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enhanced Explore Dashboard - SDG 7 Energy Analytics (20    main()in__":
_ma== "_f __name__ LITY")

iNCTIONAEARCH FUHANCE SED TO EN("\n❌ FAIL  print
      se:)
    elg"er testinCtrl+F5 afthe with wser cacn🔄 Clear broprint("\           
 
    nfo")access ity ci electrips displaypu. Check: Point("   6
        prbels") lath countryow wipins sh: Location . Verifyt("   5       prin)
 ions"estany sugg See GermType 'Ger' →int("   4.       prn map")
  pin ocation dia → See lo Click on In("   3.     printns")
   estio suggSee Indiaearch bar →  'Ind' in sType("   2. int      pr")
  /explore/7.0.0.1:8000: http://12  1. Go to(" rint)
        pTo test:"\n🧪 int("        pr 
   n")
    n selectio dropdowsearch andzed roni"   ✓ Synch(     print")
   ormationcountry infps with sional popu Profes   ✓print("  
      on pins")ing locati bounc✓ Animatedprint("   ")
        onsstin suggentage iperceess city accctri"   ✓ Ele print(       ries")
ted countor selecrs fns/markeLocation pi✓ t("           prin")
you typegestions as l-time sug ✓ Reat("  rin      p")
   optionsuntryns with coch suggestiohanced searnt("   ✓ En  pri      atures:")
\n🎯 New fe  print("
      " * 60)rint("=  p)
      ANCED!"INS ENHCATION PAND LOIONS WITH SUGGEST"✅ SEARCH  print(   
     * 60)" + "=""\nnt(     pri
   f success:
    i()
    ctionality_fun_searchhances = en    succes""
"tionality search funcceto enhanion "Main funct    ""ain():
ef mlse

deturn Fa r       
e}")le: {iting fiError wrprint(f"❌   
       e: as Exception   exceptue
 rn Tr   retu  )
   n pins"nd locatiogestions a sug search withlly enhancedfuSuccessint("✅       pr)
  _htmlenhancedite(wr          f.s f:
  8') aoding='utf- ench, 'w',file_patopen(html_h  wit       try:
   '
    
 
</html>''
</body>   </script>
       }block';
  display = '.style.Section')esulttById('renemetElment.g docu
              `;
         iv>     </d        n>
   toy Again</butload()">Tr"location.renclick= mt-3" oprimaryn-s="btn btn clas <butto          
         ge}</p>sames       <p>${       
      ailable</h3> Unavalysispx;">Anottom: 154; margin-b5640lor: #8"co<h3 style=            i>
        ></20px;"in-bottom: 07; margolor: #ffc1rem; ce: 4t-siz"fonstyle=riangle" on-tfa-exclamaticlass="fas          <i        e">
    und-messag"not-foclass=iv          <d  = `
     .innerHTML ction')d('resultSeementByIetElt.g  documen    
      essage) {Error(mhow sonuncti       f}

  }
               lock';
     = 'bisplaytyle.dn').sesultSectioentById('remElument.get     doc            {
!show)        if (
    'none';lock' :  'b = show ?displayle.ection').sty('loadingSentByIdt.getElem documen     
      how) {ding(sLoaunction show     f

       }});
    e sive: truonspt, { rece], layou [trat',ieChary.newPlot('p    Plotl
        ;
         }ion`
   ibutSource Distrnergy - EountryName} title: `${c             
   out = {   const lay     ;

       }     
    ole: 0.3          h
      b6'] },'#9b59', 98db '#34#27ae60','#e74c3c', 'ors: [ker: { col   mar        ,
     pe: 'pie'  ty            Other'],
  , 'clear''Nuwables', ls', 'Rene['Fossil Fue  labels:              erShare],
 hare, othearS, nuclwableSharerene, are[fossilShues:       val       ce = {
   t traons     c

       rShare);lea nuc -hareableS- renewossilShare - f00 h.max(0, 1= MatrShare const othe    ;
        wableShare)ne, 25 - re= Math.max(5Share nuclearconst            leShare);
  renewabmax(20, 70 -are = Math.fossilShnst           co));
   * 0.3ccesscoords.an(60, 15 + (Math.miShare =  renewablenst        co {
    , coords)ountryNamert(cChaerEnergyPieon rendncti
        fu     }
e });
   : truresponsive { ], layout,rt', [traceableChanewot('re.newPl      Plotly};

        
          (%)' }ble Share tle: 'Renewais: { tiax        y  
      ' },: 'Yeartitle: {    xaxis       
       Forecast',rgy Growthewable Enetitle: 'Ren                {
  layout =     const
          };
        }
 ', width: 3  '#27ae60ne: { color:    li          
  re',wable Shae: 'Rene   nam          ',
   rsmarkenes+ 'li      mode:
          atter',e: 'sc         typ   h,
    eGrowtablenewy: r         ,
       rs x: yea          
     ace = { const tr       ;

    8))- 2021) * 2. + (year cess * 0.2)rds.ac 20 + (coo.min(95,r => Mathmap(yea= years.wth rot renewableGns  co      i);
      2021 +(_, i) =>: 10}, from({length Array.t years =   cons
          {rds)Name, coorywth(countbleGrorenderRenewan ctio       fun
 
        }
; true })responsive:ut, {  layotrace],hart', [ccessC.newPlot('aly    Plot

         };          %)' }
 'Access (s: { title:     yaxi          ar' },
  Ye { title: '      xaxis:        0)',
   (2021-203astoreccess FAcElectricity    title: '              {
t = layou const  
         ;
        }
    0.8 }y:  opacitdb', '#3498color:er: { rk          ma  
    'bar',   type:             ,
 Forecast: access         y  ars,
      x: ye               trace = {
onst           c1.5));

  ) *  - 2021 (yearaccess +0, coords.ath.min(10ar => Mars.map(yeecast = ye accessFor       const
     1 + i);, i) => 202}, (_({length: 10y.fromrra = Ast years  con       ords) {
   ame, cocountryNst(AccessForecaern rendtiofunc
        }
     
   e: true });sponsivre, layout, { ace2]ace1, trChart', [trainwPlot('mnelotly.         P

          };     
)' }ess (%ctricity AccEle title: '   yaxis: {           ,
  'Year' }tle: axis: { ti      x
          `, Timelinety Accesstrici} - ElecountryNametitle: `${c            {
     yout =onst la        c

       };}
         h' : 'dash: 3, dash7ae60', widtor: '#2{ colne: li              ,
  ctions' Predie: 'ML   nam   
          ',kerses+marline: '       mod,
         scatter' '       type:,
         eAccessfutur         y:        ears,
reY: futu         x
       ce2 = {nst tra  co            };

   
       3 }:  width '#3498db',color:    line: {              Data',
orical 'Hist  name:              +markers',
mode: 'lines       ,
         er': 'scatt   type          Access,
   istorical       y: h
         s,lYearhistorica   x:             race1 = {
 t tns    co
        });
         2);
   om() *  Math.rand +torac yearFss +aseAcce, bMath.min(100return                 .2;
) * 1 - 2021r = (yearactost yearF        con   ];
     .length - 1Accesscal[historissricalAcce= histoeAccess nst bas  co       
       ear => {.map(yutureYears = fAccessconst future        
     2021 + i);(_, i) =>},  10gth:y.from({lenrars = ArfutureYea   const     
     
});           3));
 () * th.randomr + MaFacto+ yearss - 20  baseAcceath.max(0,, M00 Math.min(1      return        
   * 0.8;ar - 2000)r = (yeFactonst year       co;
         s.access= coordAccess  basest        con
        ap(year => {calYears.mstoriss = hioricalAccenst hist    co
        i);> 2000 + (_, i) =ngth: 21}, y.from({lears = ArraicalYestor  const hi        
   coords) {yName,ountrChart(cderTimelineunction ren f        }

  }
       
          :', error);ering failed Chart rendle.error('❌so       con         {
) orrr  } catch (e        
                }`);
  yNameor ${countrfully fed successs renderll chart✅ Ale.log(`   conso        
                  
    coords);Name,(countryieChartergyPderEn  ren              oords);
ntryName, ceGrowth(coublnewarRe     rende          coords);
 ountryName, recast(cForenderAccess             s);
   , coordmetryNa(counhartlineC  renderTime            y {
  tr        
                ame}...`);
ntryNs for ${coug chartenderin(`📈 Re.lognsolco          s) {
  , coorduntryNamets(coarChllnderAre function 
       
;
        }rdsHTMLnerHTML = cas').inardricCetentById('mgetElemument.doc        '');

        `).join(
              </div>      
    rend}</div>">${card.t-top: 10px;; margin 0.9rem"font-size:" style=end="trdiv class           <>
         </divt}${card.uniunit">"<div class=                   /div>
 ue}<d.val>${cars="value"as     <div cl           /h4>
    .title}< <h4>${card             ">
      metric-cardass=" <div cl            rd => `
   (cas.mapL = cardt cardsHTM cons     

      ;           ] }
            y'
    nuall an.2%+3rend: '          t
          it: 'USD',       un         
    eString(),toLocalPerCapita.lue: gdp     va             Capita',
  GDP per e: ' titl               {
                   },
             
     2030'1.8% by  trend: '-         ,
         it: 'Mt'         un         
  ,Fixed(1) 1000).tomissions /ue: (co2E        val            sions',
e: 'CO₂ Emis titl            
            {  
            },        
     y 2030'+4.1% bend: '      tr          '%',
        unit:                 xed(1),
Fihare.tobleSnewa value: re              
     e',able Shartle: 'Renew         ti
               {             },
         030'
      % by 2rend: '+2.3     t       ,
           unit: '%'                Fixed(1),
 s.access.to: coordalue   v                Access',
 ctricity itle: 'Ele   t                {
               = [
   const cards           
        
     ) * 10000);andom(0 + Math.rs * 40esoords.accmax(500, c = Math.erCapitadpPconst g         
   om() * 200);+ Math.rand) ccess * 3oords.a00 - (cx(10, 5 = Math.manssionst co2Emis       co  
    20));random() *0.3) + Math..access * 0 + (coordsx(5, 2ath.mamin(95, M = Math.ableSharest renewcon            country
 based onic data alistGenerate re        // {
    rds) tryName, cooCards(counMetriction update       func }

 
                 }SDG-7.`;
  r eeded foaction nent ss. Urgccetricity aecss}% elce${aconly  has me}Na> ${countryeed:</strongical N>Crit = `<strongox.innerHTMLtB aler           
    cal';critix  'alert-boclassName =lertBox.         ae {
        els   }
         gets.`;ar-7 tSDGto reach rovement for imps. Room accescity lectricess}% eac ${hasyName} trounng> ${cstrogress:</ Protrong>GoodTML = `<sBox.innerHert          al;
      box warning'rt- 'aleame =x.classNalertBo              = 70) {
  (access >e if        } els    
 ss.`;ty accectriciccess}% eleieved ${as ach} haametryNg> ${counss!</stronAccelent Energy celg>ExstronerHTML = `<x.inn alertBo             good';
   ox = 'alert-b.className    alertBox          95) {
  ss >= if (acce                 
s;
       esrds.access = coost acc         con');
   ertBoxtById('almenetElecument.gox = dot alertBns   co{
         me, coords) NatBox(countrydateAleron uptifunc

        ;
        }yName}`)tr ${counsplayed for diults.log(`✅ Resnsole          co    
  );
        me, coordsyNa(countrderAllCharts ren         rts
  / Render cha     /   
         ;
        'block'y =yle.displaon').stctiresultSeementById('getElment.cu      do    
  s sectionw result/ Sho /  
                   ords);
  yName, cords(countretricCadateM      up  ds
    c caretriate m Upd //            
         oords);
  ame, countryNAlertBox(c     update    box
    alert   // Update            
  
        ysis`; Analrgy} - Eneme${countryNant = `tConte.texTitle')Id('countrymentBynt.getEleocume   d  tle
       date tiUp  //            
          ame}`);
 ntryN ${coults forlaying resuDisp.log(`📊    console
                            }

     rn; retu              
 ;tryName}`)for ${counle availabt ata no(`Sorry, d  showError         
     ords) { if (!co                     
ame];
  countryNates[untryCoordin= const coords    co    
      {Name)lts(countrydisplayResu  function 
              }
| 6;
tryName] |Levels[counomzo  return     
              };': 6
    6, 'France 'Germany': na': 5,, 'Argentidia': 5: 4, 'Inlia'  'Austra       
       zil': 4,a': 4, 'Bra, 'Chintates': 4 SitedUn': 3, ' 'CanadaRussia': 3,  '         = {
     evels nst zoomL  co      me) {
    Nael(countryomLevCountryZounction get
        f}
     
   0000;ame] || 30dii[countryNurn ra       ret   };
             0
 0000an': 200, 'Japgdom': 1500Kinited 200000, 'Un': rance 'F00000,: 2ny'erma   'G            0000,
 ina': 50gent 500000, 'Arndia':0, 'Ia': 60000alitr 'Aus: 600000,zil'        'Bra0,
        ina': 70000 700000, 'ChStates':d te0, 'Uni0000da': 80000, 'Cana 100ia':     'Russ   
        t radii = {      cons
      ame) {ryNRadius(countCountrytion get func    

         }e()];
  erCasyName.toLow] || [countryNameuntrs[coivelternatrn a       retu        
      };
            
    ['czechia'] Republic':      'Czech
          urma'],nmar': ['b        'Mya,
        ']of iranublic ic rep['islam   'Iran':              korea'],
 ublic of, 'rep: ['korea' Korea'  'South       ,
       ina', 'prc']ublic of cheoples rephina': ['p          'C     ation'],
 feder['russian   'Russia':              nd'],
 englain', 'britaain', 'ritk', 'great b['uingdom': ted K      'Uni         ca'],
 'us', 'ameri america', states ofnited a', 'u: ['usd States'     'Unite           
 { =alternativesconst          e) {
   tryNamcounNames(yAlternativeon getCountr     functi  }

       
  n null;      retur  
            }
                }
               }
                       }
                       }
                        
    feature;rn     retu                     ) {
      ropValue)des(p| term.inclues(term) |ludue.incopValrm || pr=== teue  if (propVal                           {
hTerms) arcterm of ser (const   fo             
                           ;
      werCase()Loto[propName].ops= prlue const propVa                        ]) {
opNameprops[pr        if (           es) {
 pertyNam proName ofropor (const p          f   
             
       ];             ereignt'
  ovIGNT', 'sERE_long', 'SOVNG', 'name    'NAME_LO        
        , admin'MIN', ', 'ADe_en', 'namEN'AME_, 'Ne'amME', 'n        'NA           mes = [
 Natyropert p   cons           es
  namproperty various ck Che       //            
   
            continue; (!props)      if         erties;
 ture.prop feast props =         con
       eatures) {esGeoJSON.f of countritureonst fea    for (c       
 gh featureshrou/ Search t /     
             );
          ].flat(  
     Name)s(countrymeernativeNauntryAltgetCo              ),
  toLowerCase(/g, '').\\s+lace(/tryName.rep       coun        
 Case(),owere.toLNamuntry     co          erms = [
 nst searchT    co        
h termste searc    // Crea      
        
      eturn null;tures) rJSON.feasGeo| !countrieJSON |eontriesG!couif (            ) {
ntryNameouJSON(cnGeontryIion findCou       funct      }

 ame}`);
  ntryN for ${couedin add Location ple.log(`✅     conso  
          
          }, 1000);     }
            ;
        penPopup()rker.ontMacurre                  r) {
  ke (currentMar     if           () => {
out(ime setT          delay
  horta safter pup   // Open po
                 
            });  
    [0, -60]    offset:          -popup',
  tom'cussName:        clas     50,
    th: 2    maxWid         {
    upContent,opup(popindPrentMarker.b         cur   
   ;
          `     
         </div>        n>
     to       </but            alysis
 Ani> Full </-line">as fa-chart="f<i class                     ry()">
   ctedCountalyzeSeleck="anbtn" onclis="analyze-utton clas         <b       
         </div>          >
     ong></span/strs.access}%<rong>${coord <stcity Access:an>Electri        <sp               "></i>
 oltfa-bfas  class="     <i               
    ">icity-infoectr class="el       <div       /h4>
      ryName}<${count <h4>                up">
   ountry-popiv class="c  <d             ent = `
 st popupCont con       
    opuped peate enhanc // Cr                     
map);
  To(       .add  
        })pinIcong], { icon: s.lnlat, coordords.rker([corker = L.marentMa         curmarker
    pin Add location     //         
 
               });   0, 60]
    nAnchor: [3 ico             0, 60],
   [6Size:        icon       
 `,        
           </div>             
    iv>tryName}</dun{con-label">$lass="pi     <div c                  div>
 -icon">📍</class="piniv          <d               >
"ontainers="pin-civ clas  <d              `
        html:           n-pin',
  e: 'locatio classNam         
      on({= L.divIcon t pinIc        consicon
    on pin tom locati cus   // Create         
    
        yName}`);troun pin for ${cng locationlog(`📍 Addiole.      cons{
      s)  coordtryName,n(counLocationPiaddunction 
        f    }

    });            : 1.5
ion     durat           e,
imate: tru      an           {
Level,], zoomng coords.loords.lat,[cp.setView(    ma        yName);
untromLevel(countryZovel = getCost zoomLe  con          to country
/ Zoom            /
       
      addTo(map);       }).ame)
     countryNntryRadius(s: getCou radiu             ss
  er thickne    // Bord              eight: 3,          wcy
      sparenill tran// F           0.4,Opacity:    fill            fill
  green  Pale      //fce7', Color: '#dc      fill
          en border    // Gre     e',  #22c55  color: '         
      {rds.lng],.lat, coole([coords L.circt =Highlighent    curr    ght
    ighlile hreen circate pale g      // Cre  
                `);
untryName}t for ${coighlighing circle hUslog(`🔄  console.          coords) {
 , yNamecle(countrithCirghtW highlition  func      }

       }
     
         coords);yName,ntrCircle(couthighlightWi      h       
   );le fallback`circSON, using in GeoJound ot f} nyName❌ ${countrg(`sole.lo   con           lse {
        } e
                     });
                : 1.5
 duration                    rue,
 animate: t             ,
      20]dding: [20,         pa     {
        bounds,.fitBounds(         map
       ounds();etB.glightHighent currds = boun   const             bounds
 tryom to coun     // Zo                  
 
        ap);ddTo(m  }).a             
 hlight'higuntry-: 'cossName       cla                  },
       cy
        arenl transpFil//            0.4 lOpacity: fil                der
       n bor Gree    //5e',       '#22c5   color:              
       er opacity// Bord               pacity: 1,   o                    ickness
  order th        // B      3,      weight:              
        fillPale green ',      // or: '#dcfce7fillCol                        e: {
 styl                re, {
   tryFeatuunco L.geoJSON(ighlight =entH     curr           
orderreen bith pale gght wighliuntry hate coCre/    /                  
           aries!`);
me} bounduntryNaFound ${coe.log(`✅ sol  con           e) {
   ntryFeatur     if (cou        
         yName);
  trSON(counGeoJInindCountryture = ftryFeaount c  cons       ta
   GeoJSON dary in d the count  // Fin                
 
     ...`);GeoJSON dataName} in  ${country for️ Searchingnsole.log(`🗺  co          
s) {yName, coordries(countrlBoundathReahtWilign highio       funct

       }
  );Name, coordstryionPin(coun    addLocat     ighting
   y highlf boundardless oin regar location plways add      // A  
      
          }      ;
      s)oord, cntryNamecle(couCirghlightWith      hi
            } else {       ;
   ds) coorryName,untoundaries(cohRealBlightWit   high      {
       N) eoJSOntriesG  if (cou
          ieseal boundart with rhligho higFirst try t     //     
            
     }        
  rentMarker);(curyermoveLa map.re               Marker) {
rent    if (cur           }
     ;
    ntHighlight)er(curreayemoveL      map.r   {
       tHighlight) rren  if (cu         arkers
  mghlights and hie existing   // Remov
                 ;
    n pin...`)h locatioName} wittryung ${co Highlightinog(`📍e.lol      cons 
             }
         rn;
           retu            e.`);
ur databasailable in ois not avntryName} ${coury, oralert(`S           
     );me}`countryNar: ${t found foes nodinatCoor.log(`❌ console            rds) {
    if (!coo            
          
  yName];countres[natrdiryCoo = countconst coords         e) {
   countryNamithPin(tCountryWighlighnction h
        fu       }

        });      
   ll;JSON = nuiesGeo     countr               pins');
n iolocatg sinndaries, ury bountouload culd not log('⚠️ Coe.nsol   co          
       or => {rr.catch(e              })
            y');
      essfulladed succundaries loountry bog('✅ Console.lo        c        a;
    SON = dateoJountriesG           c       {
   en(data =>         .th)
       e.json()ponsonse => resespen(r  .th           ojson')
   rld.ger/DATA/woallery/mastey/D3-graph-gcom/holtztent.hubusercongit//raw.ps:'htt fetch(         JSON
  eoies G countrad worldLo    //   
               
   ..');es.arioundntry bg cou🌍 Loading('loconsole.      ) {
      es(ritryBoundaCounon loadti      func     }

;
     , 2000)    }       e);
 (countryNamultsisplayRes          d
      ng(false);oadi  showL     
         out(() => {setTime          
  sy result displang andetchita fe damulat// Si             
  
         ue);owLoading(tr  sh
          Show loading      //            

       ame);ountryN(cthPintCountryWi  highligh        pin
   ntry with couighlight   // H
                     e}`);
countryNam: ${🔍 Analyzingonsole.log(`     c    ryName;
   county = trentCounrr    cu      }

             return;
          
       try');ounr a c fot or searchease selecrt('Pl    ale           ame) {
 tryNoun     if (!c       
      e;
      luvapdown').ntryDro('couentByIdtElem.gement docu                        
      ue.trim() ||nput').valcountryIById('t.getElementme = documenst countryNa    con        ry() {
edCountnalyzeSelectfunction a       
 
   }
     in(country);WithPuntry highlightCo        on pin
    with locatiighlight hdiately // Imme               

        none'; = 'isplaystyle.dns').Suggestioearchd('smentByIent.getEledocum            ry;
e = countdown').valutryDropntById('counlemet.getEen   docum         country;
 t').value =ountryInpud('cByIt.getElement    documen                
 ry}`);
   ch: ${country from searlected countSeog(`🎯 .l   console   {
       untry)earch(coFromSlectCountrytion seunc
        f       }
e');
 mpletcoearch setup hanced sle.log('✅ Enconso         
                });
              }
          ));
   nt('input'venew Ent(tchEveis.dispa      th            stions
  show suggeut event to r inp   // Trigge              > 0) {
   e.length his.valu      if (t        
  nction() {ocus', fuistener('fddEventLt.archInpu sea         lue
  s va hacused andnput is fo when igestions// Show sug         
        });
                      }
          ne';
   isplay = 'no.style.dsuggestions                    target)) {
(event.s.containsestionsugget) && !s(event.targput.contain(!searchInif               {
  ent) (evionck', functr('cliListeneent.addEvent     docume
       g outsidn clickinhe wuggestions   // Hide s
                        });
 
            }      e);
      his.valuPin(tthCountryWihighlight                   one';
 display = 'ntyle.ons.s suggesti                  
 value;e = this.valuut.hInprc     sea              {
 lue) his.vaif (t        {
        ion() ', functnge'chatener(isn.addEventL   dropdow    
     n change dropdowetup // S         
        
      );      } }
                     one';
'nlay = e.dispns.styl suggestio                   se {
     } el        ck';
   y = 'blotyle.displauggestions.s           s         in('');
       }).jo   
             `;                     v>
  </di                  
        ss}%</span>oords.acces">${ccesstion-aclass="suggen c <spa                          n>
     /spa>${country}<"-textions="suggest <span clas                              >
 n-icon"></iestiogg sualtrker--map-maass="fas fa   <i cl                   
          ountry}')">Search('${ctryFrom"selectCounlick=" oncestion-itemsugg"lass=    <div c                      `
    return               
        untry];tes[cordinaooyC= countrords     const co              
      > {try =s.map(counche = mat.innerHTMLnsggestio          su
          accesselectricity icons and h ions witstggeenhanced su Create      //          {
      0)es.length > (match    if         
                  hes
  6 matcow top / Sh(0, 6); /     ).slice
           )aluees(v).includLowerCase(ountry.to       c          try => 
   uner(cofilties.hes = countrmatc  const               untries
hing comatcind  F     //              
                      }

       return;                  
  'none';y = .displaons.style    suggesti             ) {
    < 1alue.length     if (v                  
         );
m(se().triCaweralue.toLo this.v =st value       con
         function() {r('input', tListeneEvenchInput.addarse             
  
         estions');searchSuggById('etElement document.gs =ionggestt su   cons    t');
     ountryInpuId('cmentByt.getEle documenput =st searchIn       coninput
     h ed searcancup enh // Set           
    ;
           })        
 ion);ild(optendChwn.app      dropdo         
 ntry;= cout n.textConten    optio     
        country;ue = option.val               option');
t('menateElecument.creption = dot o   cons           {
  y => rEach(countries.fo    countr
        own');tryDropdcounById('nt.getElemeocument ddown = droponst  c       n
   ate dropdow/ Popul   /     
               y...');
 tionalitarch funcced se up enhaningSett'🔧 og(e.l    consol
        () {rchancedSeaEnhupion setnct       fu      }

 }
          ror);
    ed:', erion failalizat initiMaperror('❌ le.onso  c             {
  error) (atch        } c
                  fully');
  essialized succap initole.log('✅ M      cons
                  
        (map);).addTo }           18
    xZoom:        ma         
    ributors',Map contnStreetn: '© Opeutioattrib              {
      }.png', {yrg/{z}/{x}/eetmap.onstrile.opettps://{s}.tr('hileLaye   L.t          
                 ], 2);
  , 0iew([20map').setV.map('= Lmap                {
      try      
              
.');ing map..tializlog('🗺️ Ininsole.          co{
  ap() tializeMnition i    func);

            }!');
essfullylized succboard initiaDashle.log('✅   conso      ies();
    oundarCountryBoad l          arch();
 edSetupEnhanc se        
   izeMap();   initial         ard...');
ashbo Dearchnhanced Sg EizinInitialsole.log('🚀        con  n() {
   d', functiontLoadeer('DOMConteentList.addEven  document   cation
   applihe e ttializ// Ini     );

   rt(es).sordinatyCoontrs(couObject.keyntries = nst cou
        contries listle couvailab  // A    };

  
        .0 }, access: 99277208.: 1583, lng{ lat: 14.0': 'Vietnam          },
  99.0 7, access: lng: -66.589: 6.4238, uela': { lat    'Venez     ,
   ss: 99.7 }658, acce, lng: -55.7-32.5228y': { lat: 'Urugua            00.0 },
ess: 1acc: -98.5795, 83, lng39.82 lat: es': {atSt    'United 
        100.0 },60, access:  lng: -3.43 55.3781,{ lat:m':  Kingdo    'United      ,
  : 100.0 }ssce1.1656, aclng: 38.3794, at: 4ne': { lrai      'Uk3 },
      ess: 57.903, acclng: 32.2.3733, : 1latganda': { 'U        },
     s: 100.0acces2433, 5.7, lng: 3lat: 38.963y': {     'Turke     9.8 },
    access: 9100.9925,ng: 700, llat: 15.8: { and'  'Thail        },
   .8ss: 38ce888, ac0, lng: 34.8lat: -6.369a': {   'Tanzani         },
  ss: 100.0, acce.2275 88182, lng:6.: 4{ latland': witzer       'S     100.0 },
 35, access:lng: 18.64 60.1282, en': { lat:     'Swed
       00.0 }, 1ss:cce, a-3.7492g: 0.4637, ln: 4 lat'Spain': {          0.0 },
  access: 10, ng: 127.7669: 35.9078, l{ latth Korea':      'Sou      
 ss: 84.2 },, acce2.9375 lng: 295,.55 { lat: -30a':uth Afric         'So0 },
   : 100.ccess2, a79, lng: 45.0t: 23.8859 la {rabia':udi A   'Sa
          100.0 }, access:: 105.3188,.5240, lngat: 61ussia': { l    'R},
        : 100.0 ccess a2245,ng: -8. l39.3999, lat: ': {tugal   'Por          100.0 },
access:451, 19.19194, lng: 1.{ lat: 5land':      'Po
       s: 94.8 },cces1.7740, a7, lng: 12t: 12.879 lalippines': { 'Phi        73.1 },
   ccess:  69.3451, a lng:.3753,at: 30 l: {istan'        'Pak0 },
    00.: 1ss acce 8.4689,, lng:: 60.4720latay': {    'Norw         : 62.0 },
, access530, lng: 8.67lat: 9.082{ eria': 'Nig            ,
s: 100.0 }0, acces 174.886 lng:40.9006,d': { lat: - 'New Zealan          
  100.0 },s:es2913, acclng: 5.26,  52.13at:{ lherlands':    'Net   },
       ess: 90.7accg: 84.1240, .3949, ln: { lat: 28pal'       'Ne  },
   .1 cess: 700, ac956 95.lng:: 21.9162, latmar': {        'Myan4 },
     9. 9cess: -7.0926, aclng:7917,  lat: 31.'Morocco': {      },
       cess: 99.4ac8, 52 lng: -102.5345,23.6: { lat:     'Mexico'      99.8 },
  ccess: , a58.97g: 101 4.2105, ln: { lat:ia'    'Malays,
        ss: 26.6 }.8691, acce9, lng: 46-18.766ar': { lat: 'Madagasc            1.4 },
 access: 7: 37.9062,236, lng{ lat: -0.0enya':  'K  
          100.0 },access:29, lng: 138.2548, 20 36.lat:n': {   'Japa           100.0 },
74, access:: 12.56.8719, lng { lat: 41Italy':      ',
      s: 100.0 }439, acces-8.2 lng: 29,: 53.41atnd': { lla     'Ire      00.0 },
  1ccess: a: 43.6793,.2232, lnglat: 33q': { ra  'I       
   0.0 },ss: 10acce 53.6880, 4279, lng:t: 32. la {    'Iran':      },
  s: 97.8 3, acces13.921: 193, lng.78-0: { lat: 'Indonesia'         
   : 95.2 },29, access78.96937, lng: t: 20.5a': { la  'Indi        00.0 },
  s: 1 acces9.0208,: -19631, lng { lat: 64.land':     'Ice       100.0 },
 , access:1.8243742, lng: 2{ lat: 39.0 'Greece':       0 },
     s: 85..0232, acces: -1 lng7.9465,: : { lathana'        'G,
    100.0 }ss: .4515, acce 101657, lng:1. { lat: 5many': 'Ger       0.0 },
    ess: 108883, acc, lng: 1.: 46.6034 latrance': {         'F},
   100.0 ess: , acc25.7482g: 1.9241, lnd': { lat: 6    'Finlan     44.3 },
   , access: lng: 40.4897at: 9.1450, opia': { lthi          'E99.6 },
  s: ces8025, acg: 30.6, ln.820lat: 26'Egypt': {          
   ss: 100.0 },9.5018, acce2639, lng: at: 56.mark': { lDen     '    .7 },
   access: 9983.7534, lng: -, .7489': { lat: 9cata Ri  'Cos        4 },
  s: 97. acces973,: -74.24.5709, lng: { lat:   'Colombia'      .0 },
    ss: 100.1954, acce7, lng: 10435.861a': { lat: Chin      '      : 99.8 },
ess430, acc-71.5 lng: 51, lat: -35.67 'Chile': {         11.1 },
  ess: 8.7322, accng: 1.4542, lat: 15 'Chad': { l
           0.0 },, access: 10 -106.34686.1304, lng:{ lat: 5  'Canada':           ,
7 }ess: 99.3, acc.925-51ng: , l350 -14.2lat:il': {  'Braz           
.0 },ccess: 100, a4699: 4., lngt: 50.5039 { la': 'Belgium
           ss: 92.2 },3, acceg: 90.3560, lnat: 23.685ladesh': { l 'Bang
           0.0 },1001, access: g: 14.5562, lnat: 47.51ustria': { l    'A      .0 },
  ss: 100 acce133.7751,: lng2744,  -25.a': { lat:'Australi      
      : 99.2 },ccess6167, a: -63.ng161, l lat: -38.4rgentina': {        'A4 },
    access: 99.1.6596, : 339, lngat: 28.0ia': { lerlg          'A.0 },
  100ccess: 3, a 20.168lng:, t: 41.1533: { la   'Albania'         
ess: 97.7 },100, acc lng: 67.7t: 33.9391, lanistan': {     'Afgha {
       ordinates =Cocountry const 
       ntriesith more coudinates woorntry c couEnhanced // ;

       = nulleoJSON iesGuntr   let co  null;
   er = urrentMarklet c       = null;
  ghlighturrentHi      let c= null;
  ry ntCountet curre      l;
  ap      let m>
     <scriptript>
 t.js"></sct/leafleet@1.9.4/discom/leafl/unpkg.="https:/pt srcri  <sc/div>

  div>
    <
        <//p>sis...<ing analy">Load="mt-3 class        <p/div>
     <   >
        ing...</spanden">Loady-hidsualllass="vi c       <span     >
    "status"ry" role=xt-primaer tener-bordspinlass="<div c            
;">splay: nonestyle="dion" gSectiin" id="loadsectionding-ss="loala c     <divion -->
   ctLoading Se     <!--   

  </div>
       </div>           /div>
 art"><"pieChid=    <div          on</h4>
   buti Distrirgy Source     <h4>Ene  
         ntainer">hart-coss="cladiv c       <   
           div>
        </       >
rt"></divewableCha id="ren    <div     >
       th</h4nergy Growenewable E       <h4>R
         ainer">t-contar"chclass=       <div     
     
        </div>         div>
   Chart"></ssid="acce  <div        
       ecast</h4>4>Access For    <h      
      tainer">hart-conass="c cl     <div         
  
           </div>
         div>></Chart""main    <div id=     4>
       000-2030)</hmeline (2rgy Ti     <h4>Ene        ">
   ontainer"chart-civ class=<d  
          > Charts --    <!--
                    </div>
         ->
   rted here -ll be inseic cards wiic metr<!-- Dynam          >
      icCards""metrards" id=etric-cclass="m       <div >
     Cards -- Metric     <!--       
 /div>
rt-box"><"ale" class=Box"alertiv id=    <d        Box -->
<!-- Alert                  

       sis</h2>lyry Anaounttle">CntryTiouid="c<h2           tion">
  ectSsulid="reection" "result-siv class=      <d->
  s Section -sult<!-- Re      
  
p"></div>"mad= <div i       
ld Map --><!-- Wor
        >
       </divv>
    </di>
         wn</smalldropdoct from the ing or seleearch by typther san eiou c></i> Yircle"s fa-info-c"falass=><i csmall     <
           muted">"text-ss=div cla       < 
                /div>
         <div>
    </            utton>
      </b          
       yze> Anal></iarch" fa-seass="fas <i cl                     y()">
  trSelectedCoun="analyze" onclick-primarybtn="btn ssn cla     <butto          
     <div>          
      ton -->ze But  <!-- Analy       
                   
    >    </div         
   elect>         </s          >
 y...</optionntr coulect a">Seon value="    <opti                n">
    pdowdrountry-s="cown" clasntryDropdocouelect id="   <s             ner">
    own-contaiuntry-dropd class="co       <div
         ropdown -->- Country D        <!-     
                  </div>
            div>
     ></ons"rch-suggestis="sealasons" chSuggestisearc<div id="                   ff">
 ete="oocompl      aut                  " 
   try...or a counh fer="Searc   placehold                       
 input" ="search-t" classpu"countryInext" id=t type="t<inpu               >
     iner"contaarch-input-v class="se <di         -->
      gestions  Sugnced Enhanput with!-- Search I         <
       ner">contaiion--selectuntryss="co  <div cla        ion -->
  ect Country Sel- Enhanced<!-                

        sis</h3>nergy Analytry E/i> Couna-globe"><"fas fass= <h3><i cl          
 ection">arch-s="se class   <div
      Section -->ch!-- Sear <
       >
div   </
     >  </a
          ></i> Backrow-left"as fa-ar class="f<i              
  ndary"> btn-seco class="btnasts/"orec"/country-fref=       <a h)</p>
     s (2000-2030ionL Predictysis with M Energy Analountryctive C   <p>Intera     
    hboard</h1>ore Dasnced Expl/i> Enhach"><a-sear fas class="f><i   <h1
         tion">secr-headeiv class=" <d-->
        Section derea<!-- H     iner">
   board-contass="dash    <div cla
ad>
<body>style>
</he    </     }
  tant;
  4px !imporh:widt  stroke-         
 !important;.3) 97, 94, 0, 1(34  fill: rgba     er {
     ight:hovy-highl  .countr 
          }
   
        ortant;mpacity: 1 !ike-optro   s
         ant;rtmpodth: 3px !i stroke-wi
           portant;c55e !im#22 stroke:         ;
   rtant2) !impo97, 94, 0.(34, 1l: rgba       filt {
     try-highligh  .coun */
      esstylighting y highlndarCountry bou/*    
               }
       #2980b9;
 background:          ver {
 n:hoalyze-bt      .an
       }
     se;
      lor 0.3s eaground-co backtransition:           ter;
 poin   cursor: 
         rem;nt-size: 0.9   fo
         adius: 6px;rder-r         bo  px;
 16px ding: 8       pad    e;
 r: non     borde      e;
 hit   color: w        
 #3498db;ground:     back       {
  nalyze-btn       .a    
  }
    m;
       re-size: 1.1 font         
  59e0b;r: #f      colo   o i {
   infricity-   .elect          
    }
      : 10px;
 omin-bott   marg         t: 600;
font-weigh     
       669; color: #059         8px;
        gap:       ter;
items: cen  align-      x;
    fleplay:    dis         -info {
electricity    .    
         }
    em;
   ize: 1.2r     font-s;
       weight: boldont-    f;
        2937  color: #1f        0px 0;
  0 1gin: 0       mar4 {
      -popup hountry    .c       
     }
       
 0px;width: 20   min-         22c55e;
px solid #er: 2   bord      .2);
   0,0,0,0a(2px rgbx 1 4phadow: 0      box-s     5px;
  1    padding:      px;
  10-radius: border       te;
      whid:  backgroun          up {
ry-popnt .cou      /
 yles *Stntry Popup Cou* 
        /     }
              }
   px);
      teY(-5 translaansform:        tr{
        0%         6   }
        px);
     nslateY(-10rm: traransfo t            {
             40%    }
        eY(0);
    translatsform:an        tr      0% {
  10 80%, %, 50%,0%, 20        ce {
    unrames bo@keyf         
 }
      ;
        olid #22c55eorder: 2px s          bwrap;
  e: note-spac      whi2);
      ba(0,0,0,0.px 8px rg0 2: ox-shadow         b1f2937;
   or: # col           600;
 ght:nt-wei  fo    m;
      0.9rent-size:           fous: 6px;
  r-radide  bor          ;
x 12pxing: 6p    padd      ;
  whiteround: kg   bac;
         eX(-50%)slat: tranansform tr          50%;
   left:      35px;
     p: -     toe;
       : absolutition       pos{
     label n-.pi   
     
        }
        nite; 2s infin: bounceatio     anim
       0,0,0,0.3)); rgba(px2px 4shadow(2px  drop-lter:fi            c3c;
color: #e74      em;
      e: 2.5rnt-siz      fo   
    {con     .pin-i
       
           }
 center;t-align:      tex     e;
  : relativitionos       p     
ontainer {in-c .p
              }
       e;
   border: non        t;
   transparenground:      back    n-pin {
       .locatios */
    n StyleLocation Pistom Cu   /*  
       }
           ffc107;
  hed #er: 2px das bord           5px;
ius: 1  border-rad
          d;d: #fff3crounckg     ba       px 20px;
 60ing:   padd        center;
  align:       text-     essage {
.not-found-m              
  }
;
        0pxng: 4     paddi
        center; text-align:    
       n {ing-sectio     .load    
      }
        
 #721c24;r:        coloc;
     #e74c3 5px solid t:er-lef    bord     
   ffe6e6;ground: #      back
      al {icx.crit  .alert-bo
        
        }     856404;
     color: #;
        f39c12x solid #eft: 5p  border-l          f4e6;
d: #ffkgroun     bac  ing {
     ox.warn-b   .alert         
   }
         55724;
r: #1      colo     7ae60;
 #2solid t: 5px border-lef           #e6ffe6;
 ound:    backgr      d {
   -box.goo.alert
             }
          .1rem;
  1  font-size:       x;
   20ptom: argin-bot    m      g: 20px;
   paddin     ;
       10pxus:order-radi      b    box {
      .alert-      
         }
 px 0;
    n: 10  margi
          ld;: boont-weight    f        ;
reme: 2.5   font-siz  e {
       c-card .valu   .metri     
           }
   r;
  : centetext-align        px;
    g: 25   paddin       
  x;-radius: 15p     border     ;
  teolor: whi       c     2 100%);
#764ba#667eea 0%, (135deg, adient linear-grckground:   ba         {
metric-card         .        
     }
: 30px;
   argin-bottom           mx;
 20pp:          ga  
 x, 1fr));x(250p minma-fit,at(automns: repeplate-colud-tem gri
            grid;play:     dis       rds {
  .metric-ca    
              }

    x; 10p  padding:     x;
      10pdius: border-ra         7eb;
  x solid #e5eborder: 1p           20px 0;
  margin:           px;
 height: 400            ner {
chart-contai  .  
                  }
 ;
 nonesplay: di        ,0.2);
    0,0,0px rgba(x 30 10p-shadow: 0       box30px;
     op: argin-t       m30px;
     g:   paddin      15px;
    : r-radius  borde        : white;
  ckground ba
           on {sectiresult-       .
             }
  m: 30px;
  botto  margin-      ,0.2);
    a(0,0,0x 30px rgbdow: 0 10pox-sha        b5px;
    us: 1border-radi          00px;
  : 5height     
       #map {                
     }
 600;
   weight:font-        280;
    : #6b7  color        
  e: 0.9rem;sizt- fon
           s {estion-acces     .sugg      
     }

        ight: 500; font-we     
      1;x:      fle     t {
  on-tex  .suggesti
              }
        em;
1.1ront-size:     f       ;
  #22c55elor:   co        icon {
 uggestion-   .s       
     
 
        }m: none;der-bottoor          b {
  -childitem:lastsuggestion- .      
  
            };
   db #3498r:olo          cf8f9fa;
  nd-color: #   backgrou{
         hover m:stion-itesugge   .       
 }
      
        gap: 10px;           center;
s:  align-item      flex;
     y: laisp       d     se;
all 0.2s eaansition:    tr
         f0f0f0;solid #: 1px r-bottom  borde   ;
       sor: pointer     cur      x;
 2px 15ping: 1add      p   em {
   tion-it.sugges
        
        
        }lay: none;sp     di     
  o;-y: autlow      overf      0px;
 25x-height:   ma     1000;
    index:           z-15);
  a(0,0,0,0.gb r 0 4px 12pxhadow:    box-s  
      x 8px;8p 0 0 rder-radius:  bo     ;
      noneborder-top:         ;
   0e00epx solid #er: 2   borde
         nd: white;rou       backg0;
     t:       righ0;
      eft:            l: 100%;
    top        absolute;
 tion:       posi      s {
on-suggesti    .search
    stions */ch Suggehanced Sear       /* En
        
         }, 0.25);
52, 219 1ba(52,.2rem rg0 0 00 hadow:   box-s         ne: none;
        outli8db;
     349or: #order-col      b{
      ocus ropdown:f  .country-d       
  }
           : white;
  ndckgrou       barem;
     t-size: 1fon            : 8px;
der-radius bor           d #e0e0e0;
er: 2px soli  bord      ;
    pxx 152p 1ding:    pad
        00%;: 1       width    own {
 pddrontry-.cou              
  }
        x;
0p 20width: min-     
       {tainerconry-dropdown-count
        .       }
    );
     2, 219, 0.25 rgba(52, 15 0.2remow: 0 0 0   box-shad      none;
    ne:tli ou         8db;
  olor: #349 border-c   
        s {input:focu    .search- 
          }
        
 ease;olor 0.3s border-cn: nsitio  tra    te;
      ground: whi  back   em;
       ont-size: 1r  f       s: 8px;
   -radiu     border     e0e0;
  olid #e0order: 2px s      b5px;
      12px 1   padding:   
       width: 100%;            {
nput h-i  .searc        
  
    
        }tive;relaition:       pos      flex: 1;
    
        ntainer {t-copuh-insearc     .      
         }
  
  20px;bottom: n- margi    
       : center;ems-itlign           apx;
 gap: 15            flex;
lay: isp d        r {
   inetion-conta-selec    .country   
       }
      .2);
    ,0gba(0,0,0x 30px row: 0 10pad     box-sh;
       30px: gin-bottom      mar  px;
    adding: 25     p       x;
adius: 15pder-r         bor white;
   ackground:           bn {
 earch-sectio .s             
        }
  ter;
cenxt-align:       te      ;
0,0,0,0.2) rgba( 30pxow: 0 10px    box-shad;
        m: 30pxin-bottoarg        mpx;
    dding: 30     pa       x;
 15padius:der-r bor     ite;
      round: wh   backg         
 {tion .header-sec    
     
      
        }0 auto;in:    marg;
         px400th: 1    max-wid      
   {ontainer.dashboard-c  
              }
   
     g: 20px 0;     paddin;
       t: 100vhn-heigh         mi;
   764ba2 100%)7eea 0%, #g, #66degradient(135: linear-background          erif;
  -s, sans Arialamily:t-f  fon
              body {le>
        <sty 
cript>
   in.js"></sy-latest.m/plotl.plot.lytps://cdn="htrcscript s  <n.css">
  all.mi/6.4.0/css/t-awesomeonlibs/f/ajax/.comudflareclo://cdnjs."httpset" href=she"style rel=nk   <li
 css" />st/leaflet.1.9.4/diflet@pkg.com/lea"https://unt" href=eshee rel="styl <link   ">
tylesheet rel="smin.css"strap.ist/css/boot5.3.0/dap@/npm/bootstrnetvr.delin.jscdhttps://"ref=
    <link htle>00-2030)</ti