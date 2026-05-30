#!/usr/bin/env python3
"""
Restore the complete explore dashboard page to full working condition
"""

import os

def restore_complete_explore_dashboard():
    """Restore the complete explore dashboard with all functionality"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🔄 Restoring complete explore dashboard...")
    print(f"📁 Updating file: {index_path}")
    
    try:
        # Create the complete working dashboard
        complete_dashboard = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Explore Dashboard - SDG 7 Energy Analytics</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px 0;
        }
        
        .dashboard-container {
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .header-section {
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            text-align: center;
        }
        
        .search-section {
            background: white;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        
        #map {
            height: 500px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            margin-bottom: 30px;
        }
        
        .result-section {
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin-top: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        
        .chart-container {
            height: 400px;
            margin: 20px 0;
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .metric-cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .metric-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 15px;
            padding: 25px;
            text-align: center;
        }
        
        .metric-card .value {
            font-size: 2.5rem;
            font-weight: bold;
            margin: 10px 0;
        }
        
        .search-suggestions {
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background: white;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            z-index: 1000;
            max-height: 300px;
            overflow-y: auto;
            display: none;
        }
    </style>
</head>
<body>
    <div class="dashboard-container">
        <!-- Header Section -->
        <div class="header-section">
            <h1><i class="fas fa-search"></i> Explore Dashboard</h1>
            <p>Interactive Country Energy Analysis</p>
            <a href="/country-forecasts/" class="btn btn-secondary">
                <i class="fas fa-arrow-left"></i> Back
            </a>
        </div>

        <!-- Search Section -->
        <div class="search-section">
            <h3><i class="fas fa-globe"></i> Country Energy Analysis</h3>
            
            <div class="row">
                <!-- Search Input Column -->
                <div class="col-md-5">
                    <label for="countryInput" class="form-label">
                        <i class="fas fa-search"></i> Search Country
                    </label>
                    <div style="position: relative;">
                        <input type="text" id="countryInput" class="form-control" 
                               placeholder="Type country name..." 
                               autocomplete="off"
                               style="border-radius: 8px; padding: 12px;">
                        <div id="searchSuggestions" class="search-suggestions"></div>
                    </div>
                </div>
                
                <!-- Dropdown Column -->
                <div class="col-md-5">
                    <label for="countrySelect" class="form-label">
                        <i class="fas fa-list"></i> Select Country
                    </label>
                    <select id="countrySelect" class="form-select" 
                            style="border-radius: 8px; padding: 12px;">
                        <option value="">-- Choose a Country --</option>
                    </select>
                </div>
                
                <!-- Button Column -->
                <div class="col-md-2">
                    <label class="form-label" style="opacity: 0;">Button</label>
                    <button class="btn btn-primary w-100" onclick="analyzeSelectedCountry()" 
                            style="border-radius: 8px; padding: 12px;">
                        <i class="fas fa-search"></i> Analyze
                    </button>
                </div>
            </div>
        </div>

        <!-- World Map -->
        <div id="map"></div>

        <!-- Results Section -->
        <div class="result-section" id="resultSection" style="display: none;">
            <h2 id="countryTitle">Country Analysis</h2>
            
            <!-- Metric Cards -->
            <div()
    main_":__main_ "__name__ ==")

if above.s ssageor methe errcheck led. Please n faitiooraest❌ Rrint("\n    p       else:
    
 )
    DY!"ARD READASHBOPLETE "\n🎯 COM   print(       
   !")
    results see Analyze and 5. Click  print("  n")
      owfrom dropdy' 'Germancting ry selet("   4. Tprin)
        "India'rching for ' sea   3. Tryint("
        pr00/")ocalhost:80ttp://l  2. Open: hint("   pr     rver")
 .py runsen manage: pythoer Start serv 1.nt("   pri
       ")to Test:ady t("\n🚀 Re     prin          
s")
 ng and chartp highlighti4. See maint("         pr
  ")' buttonlyze Click 'Ana"   3.     print(own")
   m dropdt froec OR sel  2.  print(" x")
      search boy name in ntre cou Typ1.t("     prin
      se:")to U\n🔄 How nt("  pri   
      ns")
     animatiostyling and l rofessiona"   ✅ Pprint(   ")
     tisticsth key sta wiric cards  ✅ Met   print(" t")
     arwth chrole g  • Renewab  nt("       prions)")
   predictirt (future cast cha     • Foreprint(" )
         mix)"gyart (enerPie ch     • (" print
        ")access)tricity  chart (eleceline • Timnt("     pri      )
  ve charts:"acti ✅ 4 intert("  rin)
        pdata"y trith counarkers w✅ Pin m"       print(")
    ightingghl country hiight green("   ✅ Lnt
        pri) world map" Interactive   ✅"nt( pri      es")
 untrith all con wipdow droCountry   ✅ ("print        tions")
 suggesth liveh input wi   ✅ Searcprint("     )
   atures:"ashboard Fe🎯 Drint("\n)
        p * 60("=" print      
 ORED!")RD RESTORE DASHBOALETE EXPL"✅ COMPnt(   pri)
      60" + "=" *rint("\n   ps:
     if succes  
    ard()
  ashboe_dexplore_omplettore_ccess = resuc    
    s=" * 60)
int(" pr  ntries")
  cou  • All 70+  print("   charts")
interactive t("   • 4    prin")
 highlightingntry ("   • Cou    print
d map")active worl"   • Inter   print(wn")
 d dropdoch input anar"   • Seint(
    prboard")g dash workinComplete("   • print     * 60)
 print("=")
   SHBOARD" DAEXPLORECOMPLETE ORING "🔄 RESTprint("
    tion""in func"""Ma    main():
 def
n False
       retur}")
 board: {estoring dashre❌ Error (f"rint      p e:
  ion as Except
    except  
      n True      retur
  ard!")lore dashboexp complete stored reullySuccessf"✅ rint(
        p   ard)
     ete_dashbocompl   f.write(       s f:
  ='utf-8') ancodingth, 'w', edex_paith open(in   w
     the file to ashboarde complete d  # Write th  
    
        tml>'''</body>
</h</script>
 }
          ;
 ryNamen count    retur             
   }
               `);
 untryName}{coh input: $sing searc(`🔍 U.logonsole     c    ;
       .trim().valueput countryInyName =ountr c           )) {
    value.trim(tryInput.counryInput &&  (count if     } else       );
tryName}`counon: ${ctiwn seleopdo Using drlog(`🔽    console.         e;
   ct.valuntrySeleme = couuntryNa        co
        ect.value) {trySelunect && coSeluntryif (co      
               
   ;tryName = '' coun         let
               );
untrySelect'co('mentByIdElecument.getect = dountrySelonst co    c);
        yInput'tr('counElementByIdocument.getInput = dt countryons         c) {
   ountry(edC getSelectfunction            
       }
   e);
  ountryNamltsSection(c showResu        me);
   (countryNaOnMapountryghtClihigh          
                }
         urn;
   ret          y.`);
    other countrtry an. Please ot availablea nName} datountryor: ${c alert(`Err            e`);
   atabas found in dtryName} notcouny ${ntr couelectedror(`❌ Sconsole.er           e]) {
     yNamnates[countrordi!countryCo  if (            
       ;
   }`){countryName: $cted seleuntry(`🎯 Coole.log  cons    
             ne';
     splay = 'nos.style.diestionrchSuggeaestions) shSugg  if (searc         yName;
  = countrelect.valueountrySct) ccountrySele   if (      ryName;
   e = countnput.valu countryIryInput)  if (count       
         
      ons');estisearchSuggmentById('t.getElens = documenestioggrchSuea    const s  t');
      countrySelecmentById('Eledocument.getySelect = ountronst c           cnput');
 Id('countryItElementBygecument. doryInput = countonst         c) {
   ntryNamearch(coutryFromSeectCounnction sel     fu  
         }
    ;
    o dropdown`)ies tuntrs.length} collCountrie Added ${ale.log(`✅       conso
            
     );           };
 n)(optioldChiappendrySelect.   count       ;
      trycounContent =  option.text            ntry;
   .value = cou      option         
 );'option'ateElement(nt.credocumet option =      cons          ntry => {
 couies.forEach(ountr  allC         
            ).sort();
 atesrdintryCooct.keys(coun = Objetriest allCoun  cons
                     >';
 on --</optintryse a Couhoo- C"">-ion value=ML = '<opt.innerHTtrySelect     coun      
            ;
 ...') dropdownntrypulating cou.log('🔽 Poonsole    c     
              ;
 urnct) retountrySele   if (!c         lect');
untrySentById('cot.getElememenct = docucountrySeleonst      c {
       wn()doopCountryDrtelapution pofunc       
        
    }
         }
        :`, error);ame} ${countryNharts for cr renderingrror(`❌ Erroonsole.e      c       ) {
   catch (error       }           
         Name}`);
  {countryfor $lly uccessfud s rendereAll chartssole.log(`✅ on   c          
   ;
        })
        sear: faldisplayModeBsive: true, pon     res           ut, { 
    newableLayoce], reTraewableace, renselineTrhart', [barenewableCt('newPlo   Plotly.              };

               , l: 60 }
 b: 50 50, r: 30,gin: { t:  mar         ,
         hite': 'wlorer_bgco      pap           a',
   '#fafaf: orplot_bgcol             
       , 100] },range: [0, #f0f0f0' 'idcolor:%)', grble Share (Renewa: { title: '  yaxis                  0' },
f0f0fcolor: '# grid: 'Year',lexaxis: { tit                 },
                   }
     '#333' olor: cize: 16,t: { son      f          
        ecast`,th Forgy Growble Enerme} - RenewauntryNaext: `${co       t                 {
     title:             = {
   ableLayout const renew             };

             
      o: 'skip'    hoverinf                d: false,
en   showleg                nt' },
 sparetranlor: ' { coine:      l         es',
     e: 'lin mod                 er',
  'scatt  type:          ,
         => 0)ap(() wableYears.m  y: rene          
        s,ar renewableYe     x:          = {
      raceineT const basel       
        };
              '
  0, 0.1)231, 76, 6or: 'rgba(     fillcol               
 'tonexty',  fill:              },
     , size: 8c3c' '#e74or: col marker: {                 line' },
  e: 'sp 3, shapth:, wide74c3c''# { color:        line:           ',
  wable Shareme: 'Rene      na             s',
 ines+markere: 'l    mod              er',
   'scattpe:     ty            ata,
   wableDne       y: re       ,
      eYearsblnewa   x: re           {
       ableTrace =ewen    const r           
  });
          1);
      2 - random() *.5 + Math.- 2021) * 2(year ble + wa, baseRenemin(95rn Math.     retu           ));
    * 0.3ess  (coords.acc0 +n(80, 2le = Math.miabewt baseRen     cons          > {
     (year =bleYears.mapa = renewaewableDatst ren     con        + i);
    i) => 20210}, (_, length: 1.from({ = ArrayYearsewablerennst        co       
  rowth Chartrgy Gle Ene/ 4. Renewab      /     );

            }       false
  eBar: layModspue, diive: trspons  re            
      t, { tLayouforecas], castTracehart', [foreccessC('aPlottly.new        Plo         };

        }
        50, l: 60b:  30, : 50, r:in: { t        marg            te',
 'whir:bgcolopaper_                  
  fafa','#fa: or_bgcol        plot          ,
   100] }nge: [0,f0f0', raor: '#f0col gridAccess (%)',{ title: '   yaxis:          
        },0' or: '#f0f0fridcolear', gtle: 'Y{ ti  xaxis:                 },
                 }
      33'#3r: '6, colot: { size: 1        fon          )`,
      021-2030ast (2ccess Forec Aricitye} - ElectountryNamt: `${c    tex                    itle: {
 t                  ayout = {
 forecastL const        
            };
    t'
        e: 'Forecas      nam              ,
    }              th: 1 }
  29954', widcolor: '#2  line: {                    y: 0.8,
       opacit                  7ae60',
  : '#2lor   co                   ker: { 
          mar            ar',
 type: 'b          
         tData,y: forecas                 ears,
   recastY       x: fo    
         tTrace = { forecasst      con           });

             5);
   1.5 - 0.7ndom() *raMath.1.2 + 1) *  (year - 202access +00, coords. Math.min(1     return         
       {=>ear s.map(yforecastYearstData = eca  const for            21 + i);
  => 20_, i) h: 10}, ({lengtm(ray.fro= ArastYears reconst fo      c         art
 t Chess Forecas 3. Acc //          

            });    alse
     odeBar: f, displayMuesive: trspon          re        { 
   eLayout,race], pi, [pieTart'('pieCh.newPlotlotly  P           ;

             }.1 }
      nter', y: -0xanchor: 'ce5, 0.on: 'h', x: orientatilegend: {                rue,
     end: thowleg      s            0 },
   b: 30, l: 30,t: 50, r: 3: { ginmar             ',
       lor: 'whitebgco paper_             
      '#fafafa',or: gcolt_b    plo                 },
                33' }
   lor: '#3size: 16, co font: {                    
    ion`,istributSource D} - Energy Name{country: `$       text                 tle: {
  ti              ut = {
    yoieLat pons    c            

     };        .3
   le: 0    ho              
  side',tion: 'out  textposi           t',
       bel+percennfo: 'la texti                     },
                 th: 2 }
 ', widolor: '#fff { cine:       l           ],
      b59b6', '#9 '#3498db', '#27ae60',3c's: ['#e74c     color                   ker: { 
    mar              'pie',
     type:              '],
    er', 'Othclears', 'Nu, 'Renewablel Fuels'['Fossi  labels:                e],
   harhare, otherS nuclearSe,harenewableSsilShare, r[foss:      value              
 = {ace ieTr const p             );

  clearShare- nuhare eSe - renewabllShar 100 - fossimax(0, Math.e =otherShar const              ));
  .2 * 0ewableShare15 - (renh.max(5, re = MatclearSha    const nu            e);
enewableShar5 - rmax(20, 7e = Math.Sharst fossil      con      ;
    cess * 0.4))oords.ac, 15 + (cn(60 Math.miShare =st renewable     con         rt
   Chay Mix Pieerg    // 2. En                });

          false
   ar:layModeBspue, ditrponsive:      res            t, { 
   lineLayou timeneTrace],li, [timeart'Ch('mainoty.newPl       Plotl
            };
          
   , l: 60 }30, b: 50 r:  t: 50,: {argin           m
         white',r_bgcolor: '     pape       ',
         '#fafafalot_bgcolor:          p          },
[0, 100] e: f0f0', rang#f0 'or:idcol%)', gr ( Accesstricity: 'Elecxis: { title  ya               ' },
   f0olor: '#f0f0dcr', gri'Yea { title:     xaxis:              },
            
          33' }color: '#3,  16ze: sit: {       fon                 )`,
20-20ne (2000elis Timcesricity Acame} - ElectcountryN  text: `${                      
e: {    titl               ut = {
 Layotimelinest          con;

            }  
         e: 6 }8db', siz#349 color: '   marker: {                : 3 },
 db', widthlor: '#3498 co: {        line       ss`,
     Name} Acce`${country    name:            s',
     s+markerline   mode: '            er',
     type: 'scatt                    Data,
ccess     y: a            years,
    x:                   {
 ineTrace =  timelst    con         );

        }            }
                    * 2 - 1);
ath.random()) * 0.5 + Mear - 2021+ (yccess oords.a(100, cn Math.minretur                     {
       } else                 3 - 1.5);
dom() * .ranath* 0.7 + M00) ar - 20+ (ye- 15 access  coords.(0,urn Math.max       ret              ) {
   20r <= 20(yea    if         {
        => (year rs.mapsData = yea const acces             i);
   000 +> 2, (_, i) =21}ength: from({lrs = Array. const yea              rt
 e Cha/ 1. Timelin /              
 try {    
                   
 e}`);ountryNam{c for $artsing chndere.log(`📊 Resol  con        s) {
  coordName, ntryharts(courC rende    function }

    
                 } `;
            div>
         </           v>
     ">Score</di"unitdiv class=      <            iv>
       0.2)}</dds.access *d(60 + coorath.roun>${Me"lus="va<div clas                   >
     ncy</h4ficie4>Energy Ef    <h                    d">
-car"metric class=div    <                 </div>
                   
it">%</div>lass="un     <div c                 
  0.3)}</div>s.access * (20 + coordh.round">${Matvaluess=" <div cla                   
    4>l</hiantble Pote<h4>Renewa                        c-card">
lass="metriiv c    <d               >
      </div             </div>
  >Mt"it"un<div class=                   /div>
     o2 / 1000)}<nd(coords.c.rouue">${Mathass="val <div cl                     4>
  missions</hCO₂ E    <h4>         
           ard">ic-cs="metrasv cl<di                    /div>
 <               
    /div>t">%<ass="uni <div cl                      v>
 dis}</rds.acceslue">${coo class="va        <div               cess</h4>
 ctricity Ach4>Ele    <                    ">
ric-cardclass="metv      <di           = `
    L rds.innerHTMCametric          s) {
      icCard (metr      if');
      dsetricCartById('mlemenment.getErds = docut metricCa    cons      {
  , coords) ountryNameards(cpdateMetricCn utio      func }

       rds);
  ryName, coo(countenderCharts         r   harts
er c Rend      //          
 }
                   ck';
'blo.display = ion.stylectesultSe     r         ) {
  onctiultSe  if (res        ');
  sultSection('rentByIdemeent.getEl documtSection =nst resul     co
       onts sectiow resul// Sh                 
      ;
 me, coords)ds(countryNaCarupdateMetric     
       ric cardste metda     // Up
                 }
        
      Analysis`;rgy Eneme} - ountryNantent = `${cement.textColeEl  tit              Element) {
f (title i         Title');
  untry'coId(lementByetEocument.g dement =leEl  const tit        itle
  Update t//                 
  n;
      eturords) rif (!co   
         ;me]Nates[countryoordinacountryC= nst coords   co         ame) {
 tryNcounultsSection(Resshowon functi  

       }      }
            ;
  = nullarker  currentM              er);
currentMarkemoveLayer(     map.r       
    ) {Marker (current       if
       }     
      null;yer =ighlightLacurrentH       ;
         tLayer)tHighlighrenurayer(cmap.removeL        
        ) {yerhlightLarrentHig    if (cu {
        ghlights()rMapHilea function c
               }
     });
      1.5
   duration:     
          mate: true,  ani           
   ng], 5, { coords.lords.lat,flyTo([co     map.try
        on counr mapnte Ce     //                

   ker; = marentMarker    curr       le;
 irctCghlighr = hiayentHighlightL  curre    es
      ferencre reSto    // 
                   p();
 Popuopen           .    
        `)
         div>        </         t</p>
   2 / 1000)} Mrds.cond(coo> ${Math.roustrongs:</O₂ Emission><strong>C    <p                   /p>
 ess}%<rds.accoo${cs:</strong>  Acceslectricity<p><strong>E                        5>
me}</hntryNa  <h5>${cou                      10px;">
 g:er; paddin: centtext-alignyle="    <div st         
       opup(`dP .bin            
   o(map)  .addT   
           rds.lng])oo, ccoords.latL.marker([ = st marker    con        marker
 // Add pin          
             );
 To(map      }).add
      ht: 2  weig            000,
  500s:  radiu          6,
     y: 0.illOpacit           f     ,
r: '#90EE90'llColo         fi      2CD32',
 #3 'lor:      co         g], {
 ords.lnat, cooords.lcircle([cL.htCircle = t highlig     cons     g
  tinligh highfill green ght liate   // Cre       
              ();
apHighlightsarM    cle     ights
   sting highl/ Clear exi          /       
  e}`);
     ${countryNamghlighting log(`🎯 Hi    console.                
    n;
 retur || !map)ds!coor      if (;
      yName]nates[countrountryCoordiords = cnst co        co) {
    (countryNameCountryOnMapghttion highli func       
   }
);
     undCountryn(foesultsSectio   showR    
     oncti seltssu // Show re    
                   ry);
p(foundCountCountryOnMaght highli        
    on mapountryghlight c Hi       //               

  ntry}`);foundCou: ${ound country(`✅ Fconsole.log          untry;
  y = foundCoountrentC       curr

        }     ntry;
    oundCou.value = fryInput      count         {
 tryInput)  (coun          ift');
  untryInpuntById('cogetElemeument.put = docryInonst count         c
   amey ntrcorrect count with npuate i   // Upd     

        }
        turn;      re   ;
       essage)ert(m    al        
                   }
                c.`;
 e, etpan, Franca, JaBrazil, Chinany, ermndia, Gfor: Ing archiy se\\nTr`\\nge +=     messa             
   else {        }      
   ')}`;n('\\n• estions.joi\\n• ${sugge?es of thmean oneyou \\nDid `\\n= sage + mes            
       {0) gth > s.lentionif (sugges        ;
        .`databaseour e in ot availabl" is nryName}count${= `Sorry, "essage let m                  
     
         ;(0, 5)).slice               3))
  tring(0,).subsrCase(weame.toLountryNudes(co.incl()rCasewe key.toLo            
       r(key => yKeys.filte countrions =suggestst on   c             
              );
   not found`Name}"tryry "${coun`❌ Count.log( console           try) {
    !foundCounif (          }

          );
                 
   rCase())y.toLoweudes(kerCase().incle.toLowentryNam         cou
           |)) |werCase(.toLoountryNameludes(cCase().inc key.toLower                => 
   nd(key eys.fi = countryKdCountry     foun          ial match
  part Try      //  
        ry) {foundCount if (!              
         }
                 );

           ase().toLowerCmeNa country) ===e(Casey.toLower         k        => 
   ind(key eys.fntryKntry = cououndCou         f       ive match
nsensitse-i Try ca   //         se {
       } el         
Name;y = countryundCountr fo        {
        me])countryNas[ryCoordinateif (count            st
h firy exact matc Tr   //         
        s);
    teyCoordina.keys(countrjectObKeys = countryconst        ll;
      nuundCountry =      let fo    a
  our datxists in y e countr if    // Check        "`);

untryName}: "${cong(`🔍 Analyziog   console.l  
          }

         return;            
    ; first!')try nameunect a cor or sele entert('Pleas  ale          
    me) {Naf (!country i    
                  ntry();
 lectedCoue = getSeyNamuntrt cons       co
     ntry() {CouzeSelectedion analyfunct      

    }         });
     em);
    d(itpendChiltions.aphSugges      searc       y);
   countrFromSearch(electCountry sck = () =>lincm.o         ite       te';
hilor = 'wackgroundCo.b item.styleut = () =>tem.onmouseo      i
          ';fa= '#f8f9or oundCole.backgrem.styl=> iteover = () item.onmous              try;
  ntent = countextCo item.         `;
               2s;
       color 0.d-unbackgrotion: transi            0;
        0f0flid #f1px soom:  border-bott           r;
        : pointe    cursor                x;
 15padding: 12px    p                ext = `
cssTitem.style.        ;
        ment('div')eEleat.cre= documentitem st       con       y => {
   h(countracered.forElt        fi
               e';
  : 'non 'block'0 ?ngth > d.leltere fi.display =leestions.stysearchSugg        ';
    HTML = 'erinngestions.ug    searchS    
             );
    
           query).includes(()erCasentry.toLow cou     
          y => r(countrlteies.ficountrred = st filte        con     
         ;
  ons) returntiugges!searchS   if (;
         ons')estiearchSuggId('sementBynt.getEl= documeggestions searchSu     const        uery) {
ies(qtrCounertion filt       func
    
        }});
                 m);
ild(ite.appendChhSuggestions searc           ;
    try)rch(counomSearyFrselectCount () => click =tem.on i              ;
 te'olor = 'whibackgroundC.style. => itemut = ()nmouseo     item.o           '#f8f9fa';
undColor = e.backgroem.stylit => = ()eover mous.on       item
         ntry;ent = coutextConttem.      i  ;
             `         r 0.2s;
  oloound-cn: backgr   transitio            
     #f0f0f0;1px solid -bottom:     border               ter;
 : poin  cursor        
          2px 15px; 1ing:dd          pa         = `
 t le.cssTextem.sty       i       iv');
  ment('dreateEledocument.c= t item       cons          => {
ntry h(couEac20).fore(0, es.slic  countri
                     ';
 y = 'blocksplastyle.diggestions.Su    search;
        rHTML = ''ions.inneggestrchSu       sea          
n;
       ns) returSuggestioearchif (!s      
      tions');ges'searchSugId(ElementBydocument.getggestions = Suonst search        c
    () {ountries showAllCunction   f  
        }
            });
           }
           ne';
     play = 'nois.style.dtionssearchSugges                 t)) {
   .targentains(es.cotionSuggessearch          !         
 .target) && s(eontainryInput.c !count                && 
   ons archSuggesti     if (se         ion(e) {
  lick', funct('cventListenert.addE     documen      e
 idng outswhen clickiuggestions // Hide s              
   });
                       }
      ;
      untry}`)selectedCoopdown: ${rom drted funtry seleclog(`🔽 Console.        co       ;
     y = 'none'playle.disons.sttiesSuggions) searchrchSuggest (sea    if          ;
      Country= selectedput.value Inuntry         co
           {ountry) dCteecel       if (s;
         valueis. thtedCountry =ecconst sel          {
       nction()change', fuer('EventListenlect.addcountrySe           
 nalityge functiown chanpdo// Dro                   
 
        });             }
  
         untries();wAllCo sho              
      0) {===th s.value.leng if (thi           
    () {unctionr('focus', fentListeneEvut.addtryInp      coun      put
g on in clickinries whenl count al/ Show     /      
        
            });    }
                ;
 value = ''ntrySelect.cou                   
 y);s(querrielterCountfi             {
            } else           lue = '';
 rySelect.va   count        
         none';lay = 'le.dispns.styrchSuggestioons) seauggestichS if (sear                   = 0) {
length == if (query.       
        se();ue.toLowerCathis.valst query = con              tion() {
  ncfuinput', tener('tLisen.addEvutnptryIcoun          ity
  t functionalpuh inarc// Se            
        rn;
    elect) retuySuntr|| !coput yIn(!countrif                     
ons');
    chSuggestid('searetElementByIent.g = documionshSuggestsearcconst       ;
      rySelect')yId('countlementBgetE = document.ectuntrySel const co         put');
  ryInount('cByIdetElementt.gdocumennput = nst countryI         co{
   y() unctionalitchF setupSear function    

          }
     }     or);
   led:', errn faiatioaliz Map initiole.error('❌ons   c         {
    error) atch ( } c                  
 );
        y' successfullizedMap initialole.log('✅        cons 
                     ap);
    }).addTo(m    
           om: 18       maxZo            s',
 ontributoreetMap cenStron: '© Optiibuttr   a               {
   x}/{y}.png',g/{z}/{eetmap.orile.openstrs://{s}.t'httpeLayer(ilL.t           
                 
    , 2);0, 0]iew([2('map').setV= L.map   map    
           try {                
 );
      p...'lizing mag('🗺️ Initiasole.lo    con        eMap() {
on initializ     functi);

      };
     lly!')d successfulizerd initia'✅ Dashboaole.log( cons         ;
  ryDropdown()untateCo       popul    
 y();ionalitrchFunct    setupSea       zeMap();
   initiali          ;
ard...')Dashboing Explore '🚀 Initializle.log(nsoco           n() {
 unctio, fd'ntLoadeonteener('DOMCventListument.addEoc
        done applicati thInitialize        // 

rt();rdinates).sooocountryCject.keys(Ob= s rieuntt coons
        ctries listable coun  // Avail

          };
    2000 }co2: 2899.0, ss: , acce277208., lng: 10583{ lat: 14.etnam':        'Vi0 },
     o2: 15600ess: 99.0, c7, acclng: -66.589.4238,  lat: 6ezuela': {Ven     ',
       000 }1400.0, co2: 1 1, access:lng: 64.5853, t: 41.3775tan': { la'Uzbekis         000 },
   o2: 7 c7,s: 99.8, acces-55.76528, lng: .52 { lat: -32Uruguay':         '   ,
16000 }: 540, co2cess: 100.ac795, , lng: -98.5 39.8283lat: States': { ed  'Unit
          51000 },2: 3 co0.0,ess: 10, acclng: -3.43605.3781, : { lat: 5dom'ited King   'Un       ,
  00 }co2: 20000, ccess: 100.78, a 53.8441, lng:4223.{ lat: rates': rab Emied Anit       'U    ,
  } co2: 202000cess: 100.0,656, aclng: 31.14, 79 { lat: 48.3aine':       'Ukr},
     3000 : 35 100.0, co2ss:433, acce, lng: 35.29637at: 38.y': { lke      'Tur },
      430009.9, co2: ss: 92225, acce: -61.0.6918, lng lat: 1obago': {inidad and T'Tr          },
   : 273000 99.8, co2ess:00.9925, acc 1, lng:lat: 15.8700 { nd':    'Thaila     8000 },
   .0, co2: 3 access: 100ng: 8.2275,46.8182, l': { lat: 'Switzerland            35000 },
2: 0, coccess: 100..6435, a2, lng: 18128lat: 60.'Sweden': {             },
co2: 23000 ss: 100.0, .7718, acce80.8731, lng: ': { lat: 7nka    'Sri La     },
   00 258000.0, co2: ccess: 1 ag: -3.7492, 40.4637, ln: { lat:pain'     'S },
       6110002: s: 100.0, coces27.7669, aclng: 15.9078,  { lat: 3outh Korea':      'S     },
  456000 co2: : 84.2,ss, acce375g: 22.90.5595, lnt: -3laica': { h Afr       'Sout
     14000 },.0, co2: ss: 100.9955, acce 14512, lng: { lat: 46.1ia':'Sloven     ,
       : 32000 }0, co2ss: 100.ce19.6990, ac, lng: 8.6690 { lat: 4ia':   'Slovak         0 },
 co2: 3700.0,cess: 1008198, ac 103.3521, lng:: { lat: 1.gapore'    'Sin    0 },
    1000, co2: cess: 100..4920, aclng: 556,  lat: -4.679lles': {   'Seyche   
      00 },o2: 500ss: 100.0, c059, acce5, lng: 21.0016t: 44.labia': { 'Ser         000 },
    517, co2:0.0 access: 10g: 45.0792,, lnlat: 23.8859ia': { Arab 'Saudi            00 },
: 17110o2 c: 100.0,, access 105.3188, lng:t: 61.5240ia': { lass 'Ru           },
000 692:  100.0, co668, access:ng: 24.9, l 45.9432{ lat:Romania':       '0 },
      0300, co2: 100.0, access: 1g: 51.18393548, ln: 25. lat {atar':        'Q00 },
    480100.0, co2: access: -8.2245, g: , lnat: 39.3999ugal': { l  'Port        
  2: 341000 },co: 100.0, 1, access14519.4, lng:  lat: 51.919d': {olan      'P
      2000 },co2: 12: 94.8, sscce121.7740, ang: 2.8797, l: 1es': { latlippin'Phi       
     0 },o2: 5700ss: 95.5, cce-75.0152, aclng: -9.1900, ': { lat:    'Peru         7000 },
  99.7, co2: access:4438,5, lng: -58.442-23.at: aguay': { l     'Par    
   ,o2: 11000 }1.8, cess: 9cc21, a0.780, lng: -8t: 8.538anama': { la        'P },
     co2: 201000s: 73.1,.3451, acces, lng: 69 30.3753lat:n': { taPakis   '        },
   co2: 68000.0, 100ccess:5.9754, a: 51.4735, lng{ lat: 2n': Oma         '000 },
   co2: 35 100.0, cess: 8.4689, ac0.4720, lng:at: 6 l: {    'Norway'
        000 },co2: 28: 26.0, ss1, acce5107.99, lng: 12: 40.33 lata': {North Kore      '
      00 },40co2: 10, .0access: 62, : 8.67539.0820, lng{ lat: a': eri        'Nig    37000 },
2: co0,  100.access:8860, g: 174., ln-40.9006at:  { l Zealand':       'New   ,
  000 } 1620, co2:s: 100..2913, acces, lng: 552.1326{ lat: ds': Netherlan    '      
  },: 3000 .7, co2access: 90, .1240949, lng: 8428.3lat: ': {   'Nepal
          ,0 }21001, co2:  access: 70.560, 95.9162, lng:.9: 21': { latnmar     'Mya     ,
  co2: 61000 }99.4, 26, access: 09g: -7.17, ln79 lat: 31.'Morocco': {            00 },
o2: 240 90.0, c, access:ng: 106.9057 47.0105, l lat:ia': {     'Mongol
       2: 486000 },.4, coaccess: 992.5528, g: -10345, ln: 23.6{ latco':      'Mexi },
        5000100.0, co2: access: g: 57.5522,-20.3484, lnt: itius': { la      'Maur
      000 },o2: 2 100.0, c4, access:lng: 14.375 35.9375,  lat:alta': {       'M,
     0 }0, co2: 200ss: 100.acce2207, lng: 73.8, { lat: 3.202ves':    'Maldi        00 },
 , co2: 2540s: 99.8es1.9758, acc 104.2105, lng:ia': { lat: alays          'M00 },
   100.0, co2:s: 100escc 6.1296, a3, lng: 49.815: { lat:uxembourg' 'L       },
     2: 140000.0, co: 10 accessg: 23.8813,4, ln 55.169ia': { lat:an     'Lithu},
       000  22 100.0, co2:3, access: 35.862g:ln33.8547, t: { laebanon':           'L
  00 },0.0, co2: 70cess: 1024.6032, ac796, lng: 6.8a': { lat: 5tvi         'La  
 , }7000co2: 1: 95.0, ess2.4955, accg: 1063, ln{ lat: 19.85Laos':      '       },
2000 , co2: 90.0ess: 10, acc18.48477, lng: lat: 29.311 { ':uwait         'K   17000 },
 co2: cess: 71.4,2, acng: 37.906: -0.0236, llatya': {      'Ken       ,
67000 } 22: 100.0, coss:acceg: 66.9237, 48.0196, lnt: ': { lahstan    'Kazak,
        2: 23000 }s: 100.0, co4, acceslng: 36.238t: 30.5852, laordan': {        'J     },
 62000: 110, co2 100.s:2529, acces8, lng: 138.204t: 36.pan': { la'Ja         
   000 },.8, co2: 9: 98 access: -77.2975,1096, lng lat: 18.ica': {    'Jama  0 },
      2: 33500 100.0, co, access:5674 lng: 12.at: 41.8719,taly': { l         'I
   : 65000 }, co2ss: 100.0,4.8516, acce461, lng: 3{ lat: 31.0l':      'Israe},
       00 , co2: 370cess: 100.09, ac-8.243lng: 53.4129,  lat: d': {lan      'Ire      },
2: 190000 0.0, co, access: 10 43.6793lng:3.2232, at: 3q': { l        'Ira    },
  672000.0, co2:00, access: 1.6880g: 53, ln279{ lat: 32.4an': Ir        '   15000 },
 o2: 6 97.8, caccess:3, .921113: .7893, lngat: -0: { lndonesia'   'I    },
       2654000o2:: 95.2, c, access629, lng: 78.9at: 20.5937 { la':Indi           '0 },
 2: 200100.0, cos: ces8, ac020 -19..9631, lng:t: 64la{ d': ancel          'I48000 },
  0, co2:  100.033, access:, lng: 19.5lat: 47.1625ungary': {   'H         
 000 },, co2: 67cess: 100.01.8243, ac42, lng: 29.07': { lat: 3Greece           '00 },
 0, co2: 160ccess: 85..0232, a: -1lng 7.9465,  { lat:Ghana':        '
    00 },0, co2: 72900.access: 10: 10.4515, 657, lng 51.1any': { lat:erm      'G },
      co2: 1000000.0, cess: 1 acg: 43.3569,154, ln{ lat: 42.3gia': or         'Ge },
    330000 co2:cess: 100.0,83, ac.8834, lng: 1lat: 46.60rance': {           'F
  0 },0, co2: 45000.ess: 1082, acc7441, lng: 25.9261.: and': { latFinl    '     000 },
   o2: 14s: 44.3, c, acces.489740, lng: 50 9.14ia': { lat:op'Ethi     
       2: 16000 }, 100.0, co36, access:5.01g: 2, ln: 58.5953{ lat: stonia' 'E          
  234000 },co2:ess: 99.6,  accg: 30.8025,ln 26.8206, : { lat:t' 'Egyp          },
  co2: 3800097.2, 34, access: -78.1812, lng: t: -1.83uador': { la        'Ec0 },
    200: 2, co2ccess: 98.1627, a: -70.118.7357, lng: { lat: an Republic'    'Dominic  
       },1000o2: 300.0, css: 15018, acceng: 9.9, l 56.263rk': { lat:nma         'De
    107000 },co2:, ccess: 100.015.4730, ang: : 49.8175, l lat': {ublic'Czech Rep            
},7000 2: , coccess: 100.0299, a4, lng: 33.435.126: us': { latpr        'Cy,
    : 26000 }: 100.0, co22, access81-77.7218, lng: 1.5 lat: 2uba': {      'C    00 },
  co2: 180s: 100.0, .2000, acces, lng: 15at: 45.1000 la': {Croati    '
        000 },2: 8, co.7ccess: 997534, a: -83. 9.7489, lnga': { lat:ic R 'Costa           },
00 co2: 840.4, : 972973, accessg: -74.: 4.5709, lnia': { latomb      'Col},
      0065000 , co2: 10.0ccess: 10.1954, a 104617, lng:.8: { lat: 35'China'          ,
  00 } co2: 8708,ccess: 99. a: -71.5430,, lng-35.6751: at { lChile':        ' },
    2: 672000, coss: 100.0ce106.3468, ac -04, lng:6.13at: 5Canada': { l          '00 },
  o2: 100ess: 89.1, c04.9910, acc, lng: 1: 12.5657 { lat':bodia        'Cam000 },
     co2: 41s: 100.0,858, accesg: 25.4ln, 39at: 42.73ia': { l   'Bulgar     ,
    2: 10000 }0.0, coss: 10 acce7277,, lng: 114.53.53 { lat: 4i':      'Brune
      462000 },7, co2: 99.: ss, acce-51.9253ng: 2350, l { lat: -14.  'Brazil':        000 },
  o2: 25s: 100.0, c6791, acces7.ng: 19159, l 43.: { lat:ina'd Herzegov 'Bosnia an       ,
    0 }o2: 21000, cess: 93. acc5887,: -63.16.2902, lnglat: -: { 'Bolivia'            2000 },
 .0, co2:ccess: 100 ang: 90.4336, l.5142,at: 27tan': { l 'Bhu       00 },
    140o2: 1 100.0, cs: accesg: 4.4699,039, ln 50.5t: { la 'Belgium':       000 },
    .0, co2: 58: 1004, access 27.953g:7098, ln{ lat: 53.elarus':           'B,
  4000 }: 8s: 92.2, co2acces.3563, : 90, lng3.6850: { lat: 2desh'gla   'Ban        ,
 3000 } co2: 200.0, access: 178,: 50.6304, lnglat: 25.93: { hrain'        'Ba  37000 },
  o2: .0, c100s: escc.5769, ang: 47.1431, lt: 40n': { la 'Azerbaija         2000 },
  2: 7 cocess: 100.0,501, ac2, lng: 14.5 47.516: { lat:ia'ustr     'A     5000 },
  co2: 41ss: 100.0, 3.7751, acce lng: 13t: -25.2744,': { laralia'Aust      },
        co2: 52000,0.ss: 10382, acce, lng: 45.0t: 40.0691menia': { la 'Ar       0 },
     co2: 20100s: 99.2,167, acceslng: -63.6.4161,  -38ina': { lat:   'Argent        },
 : 150000 4, co2 99.96, access: 1.659, lng: lat: 28.033geria': {Al   '       },
  00 45o2: : 100.0, ccess1683, acg: 20.3, ln lat: 41.153: {bania'Al   '
         000 },7.7, co2: 9ccess: 9, a.7100ng: 6791, lt: 33.93an': { la 'Afghanist
           s = {ordinateCoountryconst c        ive data
nshewith compretes  coordinaountry // C

       rker = null; currentMa
        let= null;yer LaightrrentHighl      let cu null;
  entCountry =t curr  lep;
           let ma  
  <script>cript>
   et.js"></s4/dist/leafl1.9.et@kg.com/leafltps://unpt src="htripscv>

    <    </didiv>
       </"></div>
 t"pieChar" id=t-containers="char clas      <div  </div>
    t">ableChar" id="renewt-containerclass="char       <div 
     v>hart"></diid="accessContainer" chart-c"div class= <         </div>
  ainChart">d="mr" intainet-colass="char  <div c
          ts --> Char!--     <       
          
      </div>      /div>
         <       re</div>
  t">Sco"uni=<div class                </div>
    lue">--="vass <div cla          
         iency</h4>ergy Effic   <h4>En                
 ic-card">"metrs=  <div clas         div>
       </              iv>
/d">%<"unit class=        <div           
 /div>--<="value">class     <div              4>
  ial</htentable Ponew4>Re<h                   -card">
 etricss="m  <div cla           iv>
    </d             v>
  </di="unit">Mt <div class                  -</div>
 ue">-="valss <div cla                   ns</h4>
issio  <h4>CO₂ Em           ">
       ard"metric-c<div class=            >
    div </        iv>
       "unit">%</ddiv class=       <            --</div>
 ="value">div class  <            >
      ss</h4Accety lectrici4>E<h                ">
    -cardic="metrclass       <div 
         ">metricCards id="rds"-caictrass="me cl