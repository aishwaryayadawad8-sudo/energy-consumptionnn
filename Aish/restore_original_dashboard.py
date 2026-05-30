#!/usr/bin/env python3
"""
Restore the original dashboard with separate search input and dropdown
"""

import os

def restore_original_dashboard():
    """Restore the dashboard to its original state before unifie
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🔄 Restoring original dashboard...")
    print(f"📁 Updating file: {index_path}")
    
    try:
        # Create the original dashboard HTML content
        original_content = '''tml>
<html la
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="">
    <title>Explore Dashboard - SDG 7 Energy Analy
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/b">
    <link rel="stylesheet" href="http />
    <link rel="stylesheet" href="https://cdnjs.cloudfl">
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linea00%);
            min-height: 100vh;
            padding: 20px 0;
        }
        
        .dashboard-container {
            max-width: 1400px;
        
        }
        
        .header-section {
            background: w
        
            pa0px;
            margin-bottom:0px;
            box-shadow: 0 10px 30,0,0.2);
            text-align: center;
        }
        
        .search-section {
            background: white;
        15px;
            padding: 25px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px
        }
        
        #map {
            height: 500px;
            border-radius: 15px;
            box-shadow: 0 10px 30px 
            margin-bottom: 30px;
        }
        
        .result-section {
            background: white;
            border-radiux;
            ;
            margin-top: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        
        .chart-cotainer {
            height: 400px;
            marg;
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 5px 
        }
        
        .metric- {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr;
            g
            
        }
        
        .metric-card {
            background: linear-gradient(135deg, #667eea 0%, #76100%);
        
            border-radius: 15px;
            padding: 25px;
            text-align: center;
        }
        
        .metric-card .value {
            font-size: 2.5rem;
            font-weight: bold;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <div class="dashboard-con>
        <!-- Header Sect->
        <div
            <h1><i class="fas fa-search">rd</h1>
            <p>Interactive Country Energy Analysis</p>
            <a href="/country-forecasts/" class="btn btny">
                <i class="fa
            </a>
        </div>

        <!--
        <div class="search-section>
            <h3><i class="fas fa-globe"></i> Country Energy Analysis</h3>
            
        
                <!-- Search Input Column -->
                <div class="col-md-5">
                    <label for="countryI>
                        <i class="fatry
                    </label>
            l" 
                           placeholder="Type country n." 
                           autocomplete="off"
                           style="border-;">
                    <div id="searchSuggestions" class="searc>
                </div>
                
                <!-- Dropdown Column -->
                <div class="col-md-5">
                    <label for="countrySelect" class="form-label">
        
                    </label>
                    <select id="countrySelect" class="form
                            
        ion>
                    </select>
                </d
            
                <!-- Buttoumn -->
                <div class="col-md-2">
                    

           px;">
                       ze
                    </button>
                </d
            </div>
        </div>

        <!-- World Map -->
        <div id="maiv>

        <!-- Results Section -->
    
            <h2s</h2>
            
            <!-- Metric Cards -->
            <div class=">
                <div class="metric-card">
                    <h4>Electricity Access</h4>
                    <div class="value">--</d>
                    <div class="unit">%</div>
                </div>
        -card">
                    <h4>CO₂ Emissions</h4>
                    <div class="value">--</div>
                    <div class="unit">Mt</div>
                </div>
                <div class="metric-card">
                    <h4>Renewable Potential</h4>
                    <div class="value">--</div>
        div>
                </div>
                <div class="metric-card">
                    <h4>Energy Efficiency</h4>
                    <div class="value">--</div>
                    <div class="unit">Score</div>
                </div>
        
            
            <!-- Charts -->
            <div class="chart-container" id="mai/div>
            <div class="chart-container" id="accessC</div>
            <div class="chart-container" id="renewabl>
            <div class="chart-container" id="p
        </div>
    </div>

    <script src="https://unpkg.com/leaflet@1.9ipt>
    <script>
        let map;
        
        let currentHighlightLayer = null;
        let currentMarker = null;

        /
        const countryCoordinates = {

            'Afghanistan':},
          ain()_":
    m"__main_== name__  __

if.")boveessages aor mk the erre checleased. Piltion fatora Rest("\n❌      prinse:
  el        

    ")STORED!ULLY REDASHBOARD FGINAL "\n🎯 ORIt(      prin  
        s!")
see resultyze to  Anal. Clicknt("   5ri       ppdown")
 m droroselecting f. Try    4   print("     )
a'"for 'Indisearching  Try    3.    print("out")
    mn layal 3-coluSee origin  2. "  print(")
       r (Ctrl+F5)resh browseRef  1. (" int
        pre:")dy to Usn🚀 Reaprint("\     
     )
      ─┘"──┴──────────────────────────────┴────────────└──    print("       │")
]   │  [AnalyzeDrop]  [Country  Input]  │  │ [Searchprint(" 
        ───┤")┬──────────────────────────────┬──────────"   ├────nt(   pri│")
                alysis Energy An   🌍 Country  │         print(" ")
       ────┐──────────────────────────────────────────t("   ┌───      print:")
  isual Layou"\n🎨 V   print(            
s")
  and chartghtinghighliee map "   3. Srint(  p
      ton")Analyze' but. Click '   2    print("try")
    ect counpe or sel("   1. Ty   print   
  is:") Analys3 - Direct\n   Method    print("     
      h box")
  lls in searcy auto-fintr 3. Cout("         prin")
  listrom country f. Select"   2(     printrrow")
   n apdowick dro   1. Clt("in    prn:")
    pdow2 - Drohod n   Met"\  print(              
ct")
try to seleounlick on cnt("   3. Cpri       ear")
 ns appestio suggSeent("   2.      pri)
    box" in searchmetry nacoun Type   1.("     print  
  put:")In 1 - Search  Method print("        
 rks:")WoHow It t("\n🔄        prin   
    )
  a"try datrs with counkein marint("   ✅ P     pr")
   ting highligh green fill✅ Lightnt("         priable")
  vailies atr  ✅ 128 coun(" rint)
        pve charts" 4 interacti"   ✅t(rin
        pighting")ghlntry hith cou map wi  ✅ World"    print(     ")
column)right button (✅ Analyze print("   
        umn)")middle coldown ( drop ✅ Country  "int(       pr)")
 ft columneld (lerch input fi"   ✅ Sea   print(s:")
     Featureashboard nt("\n🎯 Dpri     
   "=" * 50)( print     )
  D!"ARD RESTOREBONAL DASHnt("✅ ORIGI  pri    50)
   "=" * \n" +print("        ess:
ucc if s
   
    ard()_dashboginal_ori = restore   success 
  * 50)
   rint("="y")
    pitctionale chart fun• Complett("   
    prinill")ight green fh lng witlightihighuntry Co   • t("
    prinailable")ies av countr   • All 128t("
    prin)ut"ayomn lolunal 3-cOrigi• print("   
    ropdown") dinput andch te searpara Set("   •   prin" * 50)
 nt("=)
    priBOARD"INAL DASHIGESTORING ORprint("🔄 R""
    on""Main functi  ""
  in():e

def maeturn Fals
        r")d: {e}oarshbg da restorinror"❌ Errint(f     p
   as e:n ioept Except 
    exc  e
       return Tru      ")
ashboard!al ded originully restorsfSuccesrint("✅         p   
nt)
     _conteiginal f.write(or           as f:
f-8') g='utw', encodinpath, 'dex_inith open(     we
   to the filcontent inal orige ite th       # Wr
 
        
</html>'''ody>>
</b</script
        }
    yName;turn countr    re         
                 }
    );
  yName}`${countrh input: g searcing(`🔍 Uslo    console.      ;
      alue.trim()nput.vuntryIe = coamtryN        coun        
 {lue.trim())Input.va& countryput &ryIne if (countls } e          e}`);
 tryNamun ${coction: seleing dropdownog(`🔽 Ussole.l      con     e;
     lut.vacountrySelecame =    countryN          ) {
   .valueountrySelect && cctountrySelef (c      i   
      ;
         ''Name =  country     letlue
       put va, then inctionropdown sele: drityrio   // P                
    ct');
 'countrySeletById(mentEle.geentocum dySelect =st countr    con    ;
    Input')('countryByIdtElement document.geryInput =ntnst cou    co      {
   y()edCountrn getSelect functioown
       dropdnd  ah both input to work wituntryedColyzeSelectUpdate ana //    
           }
  
       untryName);ection(coResultsS     show
       onlts sectiesuso show r  // Al                  
 Name);
   p(countryOnMalightCountry       high
     ry on mapuntght the coately highli Immedi //     
               }
                 return;
         ;
     y.`)other countrase try ane. Pleablnot availta  daame}countryNError: ${    alert(`   
         e`);atabas dfound inryName} not ry ${countlected count❌ Se.error(`  console              me]) {
[countryNaCoordinatesntry!couif (            ts
ountry exis// Verify c     
           ;
        me}`)untryNa${coed: selecty ntr🎯 Coue.log(`   consol                 
 
   one'; 'nisplay =style.dSuggestions.ns) searchrchSuggestio(seaf           i  tryName;
count.value = lectrySet) counountrySelec      if (c   
   ountryName; = clueut.vanpountryItryInput) c   if (coun    
     downand droph input  Update bot         // 
              tions');
hSugges'searcntById(metEledocument.getions = earchSugges    const s        
elect');'countrySntById(.getElementect = documet countrySel      cons    put');
  ntryInId('couByetElement= document.gtryInput   const coun   
       me) {ountryNarch(cuntryFromSeaectCoon sel  functi
      dropdownnd search ah with boto work function try tCountelecced s// Enhan 
                }
   
    n`);pdowes to droth} countringies.lellCountr✅ Added ${aole.log(`      cons  
      
          ;    })
        option);ndChild(ySelect.appeountr    c         try;
   tent = countextConn.      optio    
       country;e =.valuon     opti      n');
     iont('optlemeeateEcument.crption = donst o   co           => {
  country s.forEach(rieallCount         option
    as an ch country// Add ea                      

  );.sort(es)ordinat(countryCoect.keys = Objriesst allCount     con        them
ies and sortl countret al        // G     
    
       on>';ry --</optiounthoose a Ce="">-- Coption valuHTML = '<ct.innertrySele   coun       lder)
  aceho plpt the firstxceons (etiing opexistr Clea    //            
   
      );own...'try dropdun coopulating('🔽 Pe.log    consol            
    n;
     returrySelect)count  if (!
          ect');untrySelco('lementByIdt.getEocumen dSelect =tryconst coun            ) {
own(ropdateCountryDtion populnc        futries
able counh all availdown witcountry dropate   // Popul       

         });      0);
}, 100        try);
    ch(testCounapan'].forEana', 'Jl', 'Chi, 'Brazi, 'Germany'India'['        ;
        untries...')ey coesting kg: T Debuole.log('🔍     cons        () => {
    setTimeout(       {
     tion()ded', funcContentLoaistener('DOMt.addEventL  documen    e load
  debug on pagAuto-run //           
       }
     }
        se;
      turn falre        );
        ice(0, 10)ates).slntryCoordinct.keys(cou Objeountries:',e cabl.log('Availonsole        c
        ); found`ryName} not{countle.log(`❌ $conso         e {
        } els       e;
    rn truretu               );
  coordsnd:`,Name} fouountrye.log(`✅ ${c   consol            ) {
 f (coords      i      Name];
try[counnatesuntryCoordids = co coor const        
   ) {amecountryNntry(Couon test      functi
  untryecific co sprify ation to venct fu  // Tes  
                 }
   ountries;
    return c      es`);
  th} countri.lenguntriesl: ${co.log(`Totaconsole           });
             );
ountry}` ${cndex + 1}..log(`${i     console      
     ndex) => {(country, iorEach(es.ftricoun       ;
     ates).sort()Coordincountrybject.keys(ountries = O  const c          
ase:'); databuntries inable coog('🌍 Availole.l cons           ies() {
trn debugCounfunctioes
        untriailable co to check avbug function       // De 
    
          }
    }
                  `;
          iv>
       </d           
      </div>                      e</p>
ablavailun chart ableew     <p>Ren                      "></i>
 px;15-bottom: x; margint-size: 48pyle="fon st fa-leaf"="fas   <i class                       ;">
  ign: centerxt-alstyle="tediv    <                    
 6;">: #66; colorght: 100% heiter;ntent: cencoify-r; justtems: cente-ilignlex; aplay: fstyle="dis  <div                 
  erHTML = `.inneChart')wabl('renelementByIdent.getE      docum      
            ;
         `          div>
               </        /div>
          <             ble</p>
   t unavailaast charrec   <p>Fo                        "></i>
  15px;ottom:n-b48px; margie: -siztyle="font-bar" sarts fa-chfass="    <i cla                        enter;">
align: c"text-div style=           <             : #666;">
100%; colorer; height: : centy-contentter; justifentems: c; align-i flexy:yle="displa  <div st                 L = `
 TMrHnert').in'accessChaementById(getElment.ocu    d                      
        `;
           </div>
                     /div>
     <                   e</p>
  navailabl ux chartp>Energy mi <                       "></i>
    om: 15px;n-bott margi8px; 4ize:e="font-sstylpie"  fa-chart-ass="fascl  <i                          ter;">
 t-align: cenyle="tex st       <div           ">
      r: #666;colo00%; ght: 1ter; heitent: ceny-con; justiftern-items: cenflex; alig="display: tyle     <div s         = `
      nerHTML Chart').inyId('pielementBtEent.gecum      do         
                 `;
              
       </div>             iv>
  /d         <            e}</p>
   errorMessag>${<p                      i>
      "></: 15px;rgin-bottom; maize: 48px"font-s style=angle"riclamation-tfas fa-ex class="      <i              ">
        gn: center;e="text-ali styliv         <d           
    : #666;">lorht: 100%; co; heig centerntent:-cor; justifyms: centelign-ite: flex; aay"displstyle=v      <di            = `
   innerHTML ').ainChartmentById('mElet.get  documen              
               gain.`;
  ase tryeaName}. Plountry for ${crtsding cha loaror`ErrMessage = nst erro        co     arts
   chessage in how error m       // S 
                     ;
   :`, error)untryName}or ${co fartsering chor rend(`❌ Errsole.error      con
          (error) {  } catch 
                    `);
      Name}tryfor ${counsfully esd succarts renderel chg(`✅ Alconsole.lo            ;

     })     
          ar: falseplayModeBis       d     ,
        true: ve  responsi           { 
       yout, wableLa], reneTrace, renewableselineTrace, [baart'newableCh.newPlot('re    Plotly             };

             }
   50, l: 60  30, b: t: 50, r:margin: {             ',
       iteolor: 'wh paper_bgc            
       a',or: '#fafafbgcol   plot_         
              },              : [0, 100]
range                        ,
 '#f0f0f0'or:gridcol                     ,
   Share (%)'e Renewabl: '    title              
      {  yaxis:                      },
                 0'
  '#f0f0for:     gridcol         
          : 'Year',title                    : { 
    xaxis               
             },         }
   '#333' 16, color: { size:     font:               
      st`,th Forecargy Growewable Ene Rene} -ntryNam${cou text: `                       tle: {
    ti                = {
leLayout t renewab       cons             };

    '
        info: 'skip hover                  
 false,gend: howle      s    
          },ansparent'  color: 'tr {ne:   li                nes',
    mode: 'li             
    r', 'scatte      type:           
   0),() => ears.map(eYblewa y: ren                   bleYears,
enewax: r                    e = {
selineTrac const ba            ine
   // Add basel            ;

      }         .1)'
     6, 60, 01, 7ba(23or: 'rg    fillcol           ty',
     'tonexill:         f          
  },ze: 8 74c3c', si color: '#erker: {       ma             },
 ne''spli3, shape: th: 3c', widr: '#e74colo: { c line               hare',
    able Sname: 'Renew          
          markers',lines+ 'de: mo               
    er',tttype: 'sca                  ,
  atanewableD re        y:           
 Years,renewable:      x           
    ace = {leTronst renewab       c       
  );
    }           2 - 1);
  .random() *+ Math21) * 2.5 ar - 20 (yenewable +, baseRemin(95turn Math.          re     );
     3)s * 0.s.acces 20 + (coordh.min(80, = Matnewablenst baseRe         co          > {
 ar =ears.map(yewableYata = reneableDt renew     cons   
        021 + i);(_, i) => 2gth: 10}, {lenArray.from(s = earrenewableY  const              th Chart
 y Growle Energ. Renewab       // 4      
          });
     alse
    ModeBar: f   display              
   ue, trive:pons res            
       tLayout, { forecas], aceforecastTrt', [harot('accessCy.newPlotlPl                };

            }
    , l: 60 0, b: 500, r: 3 t: 5gin: {ar m               ite',
    or: 'whbgcol  paper_               
   '#fafafa',: ort_bgcol  plo              
          },             
 0, 100]ge: [  ran            
          0f0f0',: '#f  gridcolor            
          s (%)',itle: 'Acces         t              
   yaxis: {         
             },              '
   '#f0f0f0dcolor: gri                   r',
     'Yeaitle:        t             is: { 
       xax                     },
         ' }
       : '#333or: 16, colont: { size  f              ,
        021-2030)`t (2 Forecasccessy A Electricite} -untryNamt: `${cotex                        {
itle:       t             ut = {
 recastLayo foconst                   };

            ecast'
 : 'For    name           
          },              
 dth: 1 }9954', wilor: '#22e: { co        lin         8,
       city: 0.     opa                   60',
'#27ae: olor          c              ker: { 
         mar          r',
 type: 'ba                
    ,astData: forec      y             ars,
 : forecastYe     x          e = {
     tTraccas fore     const   
               });
       .75);
  .5 - 0andom() * 1+ Math.r2021) * 1.2 ar - (yeess + coords.acch.min(100,   return Mat              {
     p(year =>ears.ma = forecastYDatat forecast     cons    
        i);1 +) => 202}, (_, i: 10rom({lengthray.fars = ArforecastYet    cons          
   rthast CForeca 3. Access   //           );

              }lse
     odeBar: fa  displayM             rue,
     nsive: tespo          r       , { 
    pieLayoute], [pieTrachart',pieCnewPlot(' Plotly.        
         };
               }
              -0.1
           y:           ',
        terenr: 'choanc     x               ,
          x: 0.5                'h',
  ntation:         orie          
      egend: {   l             
    : true,egendhowl      s           30 },
    0, l:b: 3r: 30, 50, : argin: { t        m        
    : 'white',lorper_bgco   pa             afa',
    fafr: '#olobgc   plot_               
         },           }
  lor: '#333'  16, cont: { size:        fo                ibution`,
urce Distrgy Some} - Ener{countryNa: `$ext          t            tle: {
       ti          t = {
     st pieLayou      con              };

            : 0.3
    hole          ',
      de 'outsiition:textpos                   ',
 l+percentlabe: 'tinfo         tex       
           },       }
       2 , width:or: '#fff'ine: { col     l        
           ],b6'#9b59b', '8d '#34927ae60',3c', '#'#e74cors: [  col                   ker: { 
        mar             : 'pie',
     type            '],
     herear', 'Ot, 'NuclRenewables's', 'Fuel'Fossil labels: [                   Share],
 hare, otherclearSe, nuShare, renewablelShar[fossies:        valu       {
       pieTrace =       const   

       rShare); nucleahare -bleSwa - renelShare0 - fossi, 10th.max(0are = MarShothenst   co              0.2));
Share *  (renewable15 -(5, maxre = Math.arShanucleonst  c     
          e);wableShar, 75 - rene20h.max(re = Matst fossilSha      con    ));
      ccess * 0.4(coords.a 15 + (60,th.min = Maare renewableShconst              ie Chart
  nergy Mix P E/ 2.      /  
          });
        lse
      eBar: faplayMod   dis                 ive: true,
nsspo      re           { 
   lineLayout, ce], time[timelineTrahart', ('mainCnewPlotlotly. P          ;

             }       }
 l: 60 50, 0, b:  t: 50, r: 3gin: {        mar          ,
  white'color: '   paper_bg                 fafafa',
_bgcolor: '#    plot                        },
           00]
 e: [0, 1       rang               f0',
  #f0f0: 'or   gridcol                  ,
   s (%)'cesty Ac'Electricitle: ti                
        xis: {   ya             },
                   
      0f0'0fidcolor: '#f       gr              ar',
   'Ye   title:              
        xis: {   xa                      },
          3' }
      olor: '#336, cize: 1{ s      font:                ,
   000-2020)`line (2Timey Access lectricittryName} - Ecoun `${  text:                
         title: {                 yout = {
timelineLa     const            
 };
             ze: 6 }
  b', si: '#3498d: { color  marker                  h: 3 },
db', widtr: '#3498e: { colo        lin           cess`,
 Name} Acryntcoume: `${ na            
       ,nes+markers' mode: 'li                  r',
 tteype: 'sca   t                ,
 cessData  y: ac                  rs,
ea: y      x          
    ce = {ineTra timelconst               
  });
          }
                       ;
  1)() * 2 - om.randMath + ) * 0.5year - 2021access + (rds.n(100, coo Math.mieturn        r           
     nsprojectio // Future                          } else {
               1.5);
    om() * 3 -and+ Math.r0) * 0.7 200+ (year - access - 15  coords.0,ath.max( return M                 
      e variation with somcal data // Histori                  0) {
     year <= 202 if (            {
       ear => years.map(yta =  accessDanst       co        000 + i);
 i) => 221}, (_, m({length: roArray.fnst years =   co              
ss Trendstricity Accet - ElecCharmeline     // 1. Ti           
        try {  
       );
        untryName}`{cots for $ing charderg(`📊 Renole.lo  cons
          s) { coorduntryName,harts(corCdeenn runctio    f
        }
   }
    ;
                 `           </div>
                ore</div>
 ="unit">Sc class   <div               iv>
      .2)}</d * 0accessrds.d(60 + cooounMath.r"value">${s=  <div clas                      
/h4>y< Efficienc4>Energy     <h         
          rd">etric-caass="m cldiv         <       
    iv>    </d          div>
      nit">%</s="uasv cl  <di               
       iv>s * 0.3)}</dces coords.acround(20 +ath.{M="value">$ss    <div cla                  /h4>
  e Potential<<h4>Renewabl                     
   >rd"-ca="metricss  <div cla                 
 </div>                  </div>
  >Mtss="unit"   <div cla                     iv>
 / 1000)}</d(coords.co2Math.round"value">${<div class=                   
     </h4>onsEmissi<h4>CO₂                        
 d">carmetric-iv class="   <d           
            </div>         >
     ">%</divnit"uss=cla  <div                  /div>
     .access}<oordslue">${c class="va  <div                    h4>
  y Access</tricit>Elec <h4                    ">
   ric-cardass="met  <div cl                  rHTML = `
cCards.inne      metri       ards) {
    if (metricC    ');
       etricCardsntById('mtElemement.gecu = do metricCards  const
           coords) {ame,ryNuntards(coteMetricCion updanct
        fu       }

 ;ame, coords)untryNderCharts(co      ren    rts
  Render cha         // 
            }
         ck';
      y = 'blodisplan.style.sultSectio      re         {
 ion) ltSect    if (resu   n');
     Sectio('resultByIdgetElement = document.esultSection ronst   c       n
  sults sectioShow re/         /
          ds);
      e, cooramds(countryNateMetricCar  upd    rds
      te metric ca    // Upda                
             }
lysis`;
   ergy AnaryName} - Enntt = `${couContennt.texteEleme titl            {
   ) titleElementif (       le');
     ryTitById('count.getElementt = documentlemenconst titleE         title
   // Update               
       ;
   ords) return!co if (        e];
   s[countryNamnateyCoordiountrcoords = c  const       {
    ntryName) ou(ctsSectionultion showResfunc     

        }   }
           ull;
 = nntMarker curre       
         er);rktMar(currenLayemap.remove               r) {
 ntMarke if (curre           }
          l;
  ulghtLayer = nrentHighliur         c
       tLayer);ighentHighleLayer(currov map.rem            r) {
   ighlightLayerentH if (cur        
   s() {ghlightMapHition clearunc   f }

          });
              n: 1.5
    duratio    e,
        te: tru anima               , {
, 5s.lng]lat, coords.coordap.flyTo([           m
 ryp on countter ma Cen    //
              r;
      kearker = marrentM      cur      cle;
ghlightCiryer = hitLantHighligh   curre  
       encesStore refer        // 
               
 opup();enP    .op           )
            `     iv>
         </d          Mt</p>
 1000)} .co2 / round(coords{Math./strong> $ssions:< Emi><strong>CO₂        <p                </p>
ss}%coords.acce</strong> ${cess:ricity Ac>Electng<stro   <p>                   }</h5>
  ntryName<h5>${cou                     0px;">
   ing: 1nter; padd cegn:"text-ali style=<div                 
   p(`dPopu       .bin
         ap)ddTo(m        .a
        ng])coords.l, [coords.lat= L.marker( marker     const  rker
      pin madd  A//       
                (map);
 To.add     }) 2
        weight:          ,
     500000: dius         ra.6,
       llOpacity: 0    fi         
   '#90EE90',fillColor:              32',
    '#32CD      color:     g], {
      coords.lnt,.lacoordsrcle([cle = L.citCirghst highli         conng
   ti highligheen fillght grte li// Crea              
 
         ts();ghlighapHi      clearM      lights
highg inistear ex/ Cl   /            
         ryName}`);
{count $ghtingg(`🎯 Highli.loconsole                      
turn;
  ap) re!ms ||  if (!coord
           yName];[countresatCoordin countrynst coords =    co       
  {me)tryNaap(counnMtCountryOghhliunction hig       f}

         );
foundCountryion(ResultsSect show       n
    ults sectio reshow  // S                
      dCountry);
nMap(foununtryOhtCohlig hig           ry on map
ht countHighlig    //     
             ;
   `)Country}ound{fy: $trund co`✅ Founog(ole.l    cons      ry;
  ndCountry = fourentCount         cur  }

             ountry;
= foundCvalue untryInput.       co  {
       untryInput)    if (co     
    meuntry naorrect coinput with cpdate       // U          }

 n;
       uret          r     
 rt(message);  ale         
                    }
                 `;
nce, etc.n, Frana, Japal, Chiraziny, Bndia, Germafor: Isearching \n\\nTry ge += `\  messa           {
       se     } el         ')}`;
    \n•\ns.join('ggestio• ${sue?\\n thesne ofu mean o yo\\n\\nDid= `   message +          {
       ength > 0) stions.l(sugge    if            e.`;
 basn our datavailable i" is not acountryName}"${y,  = `Sorrlet message               
               
  lice(0, 5); ).s               , 3))
g(0ubstrinCase().se.toLowercountryNam).includes(erCase(ow  key.toL           => 
       ilter(key ountryKeys.fns = cggestio const su            stions
   suggee lablShow avai         // 
              
          found`);nottryName}" oun${cry "unt Co`❌e.log(ol  cons           {
   ry) oundCount if (!f          

      } );
                    ())
  owerCasey.toLludes(kese().incrCaame.toLowentryN         cou      
     )) ||erCase(.toLowmecountryNacludes(rCase().in key.toLowe           
         (key =>.find countryKeysy =ndCountr fou            h
   partial matc  // Try        
       ntry) {Couound(!f   if          
        
            }   );
             
    owerCase().toLmeountryNa() === cLowerCaseey.to  k                
   ind(key =>.fyKeystrtry = counundCoun fo       ch
        sitive mat case-insen Try    //            } else {
       ame;
     tryNntry = counundCou  fo              ryName]) {
inates[countCoord(country   if          tch
t maxacrst try e      // Fi
              );
    esinatntryCoordcoubject.keys( OryKeys =nt const cou    
       null;dCountry = et foun  l      itive)
    (case-insens data in ourxists  country e/ Check if /       

    );ates)dinryCoorcountect.keys(ies:', Objountr'Available c.log(le     conso
       Name}"`);untrycor: "${ching foog(`🔍 Searconsole.l        }

            eturn;
          r        );
  irst!' fntry namelect a cou or selease enter alert('P       {
        untryName)     if (!co                
    y();
ntrSelectedCouName = getountry    const c;
        untryInput')('cotElementByIdument.ge = docutInpountryst c con           () {
ryelectedCountanalyzeSnction      fu
    }
   me);
    n(countryNasSectioshowResult          section
  how results o sAls       //           
      me);
 ap(countryNayOnMghtCountr   highli     n map
    ry o countighlight thediately h/ Imme      /
            
             }     n;
retur            `);
    country. another trylease available. Pta not tryName} darror: ${counalert(`E            );
    n database` not found iryName}ount${cted country ecel❌ Serror(`e.olons           ce]) {
     amtryNes[counCoordinatcountry  if (!
          y existserify countr V          //  
  
          yName}`);untr{coselected: $ry untlog(`🎯 Co  console.         
          ne';
   = 'noay le.displtions.styggesearchSu) sggestionsSu (searchif      ;
      tryNamealue = counryInput.vt) countntryInpucou      if (      
            );
uggestions'yId('searchStBtElemenocument.gestions = dggehSuarconst se  c          
put');'countryInmentById(Element.get docuntryInput =ou const c      
     ) {ryNameountry(countlectC senction       fu
        
     }
     });      em);
     ild(itndChappens.hSuggestioarc     se        untry);
   arch(coomSentryFrlectCouse= () => m.onclick          ite;
       'white'oundColor = ackgr.style.b= () => item.onmouseout       item
          ;f9fa' = '#f8kgroundColorbacm.style.ite () => er =ovonmouseem.it         ry;
       ntntent = couem.textCo  it            `;
                
  0.2s;lor nd-coackgrouition: b       trans         
    #f0f0f0;x solid m: 1per-bottord     bo            ter;
   : poin    cursor             15px;
   2px ng: 1   paddi            
     cssText = `e.tylm.s        ite       ');
 Element('divent.createitem = docum    const          {
   untry => forEach(co  filtered.
                     
     `;      
  '};ck' : 'none> 0 ? 'blogth ltered.len: ${fi display             y: auto;
    overflow-             ;
 0pxt: 30 max-heigh         00;
      : 10exndz-i              
  ,0.1);(0,0,0 12px rgbadow: 0 4pxx-sha    bo          
  px;radius: 8er-   bord          0e0e0;
   solid #er: 1px   borde            ite;
  ground: wh     back   
         right: 0;          ;
     eft: 0         l    
   00%; 1op: t           ute;
    tion: absol       posi        ext = `
 sTtyle.csons.sggestichSu        sear  
   '';nerHTML =gestions.inrchSug  sea
                         );
        
 (query)ludes).incLowerCase(.tountry co             y => 
  ter(countrs.filcountrieed =  filter      const 
           
      ns) return;estiougg(!searchS if         
   stions');searchSuggentById('tElemet.geocumen= dions Suggestnst searchco            ery) {
ountries(qution filterC      func       
    }
 
          });     (item);
   hildappendCtions.gesug    searchS        );
    arch(countryryFromSeselectCountk = () => clictem.on      i         hite';
 or = 'wackgroundCole.b> item.stylseout = () =mou item.on              f9fa';
 #f8Color = 'ackground.bem.style it => ()mouseover =    item.on  
          ry;ntt = coutextContenm.      ite   
            `;         
  lor 0.2s;ground-cocktion: ba  transi                   #f0f0f0;
px solider-bottom: 1   bord           
      er;r: pointcurso                   x;
  12px 15p  padding:                 ext = `
 cssTstyle.tem.          i      ('div');
ntreateElemement.c docuem =const it               y => {
 untrh(corEac0).fo 2e(0,iccountries.sl              
    `;
                
  y: block;   displa             uto;
verflow-y: a o             px;
  00x-height: 3  ma           000;
   -index: 1    z            1);
0.0,0,0,px rgba(px 12adow: 0 4-sh     box
           : 8px;order-radius b               #e0e0e0;
solid 1px    border:             te;
 hiackground: w  b              ht: 0;
         rig;
       ft: 0    le        
    p: 100%;        to    ute;
    tion: absol   posi           
  = `.cssText ylens.stchSuggestioear    s
        L = '';rHTMnneestions.iarchSugg se               
       ) return;
 ggestionsf (!searchSu    i
        gestions');'searchSugntById(lemecument.getEdos = ionchSuggestear s       const
     () {esCountrishowAlltion         func  
      
        }
 });   }
                        ';
lay = 'nonedispons.style.hSuggestiearc   s                 {
) (e.target)ns.containshSuggestio     !searc            et) && 
   e.targ.contains(Inputcountry          !          
&& uggestions f (searchS       i
         {ction(e) , funner('click'entListeaddEv   document.    ide
     cking outss when cligestionde sug      // Hi    
         
        });       
           }       
`);dCountry}teelecropdown: ${scted from dtry sele🔽 Coune.log(`ol        cons          try
  ed counlect se analyze thetomatically    // Au               none';
 splay = 'tyle.diggestions.shSuions) searcstchSuggeear  if (s                ons
  uggesti/ Hide s    /              y;
  ountrctedCe = selealuInput.v country               ountry
    cted cleut with se search inp Update  //         
         ) {Country(selected   if             .value;
 = thisuntry tedCo const selec                {
()onnge', functir('chaventListenet.addEountrySelec c   
        alityctionange fun Dropdown ch//            
       });
             }
               es();
     ntriAllCou      show            {
    === 0)alue.lengththis.v if (             on() {
  uncticus', fner('foEventListeddput.atryIn        coun
    n inputclicking on  wheiesl countr  // Show al        
      );
              }  }
         
           ;.value = ''untrySelect      co              g
n when typinown selectioClear dropd       //          ery);
    es(quntrirCou  filte             {
       } else               
'';t.value = Selecountry c                
   en typingelection whn sar dropdow    // Cle           ;
     ay = 'none'.displstions.styleggens) searchSuiostearchSuggeif (s                {
     0) h ===uery.lengt     if (q     );
      erCase(owe.toLvalury = this.t queons         c {
       , function()input'istener('addEventLryInput.       county
     litionafunctput Search in  //             
         ) return;
 trySelect !counryInput ||countif (!            
      n();
      ntryDropdowteCou     popula
       iesuntrith all con wate dropdow   // Popul                
;
     ons')estiugg'searchSId(mentBygetEleent.= documns chSuggestioear   const s     ');
    electntryScouentById('ent.getElem = documecttrySel const coun
           ut');untryInptById('co.getElemenument docnput =nst countryI    co
        () {nalityunctioetupSearchFction sfun      

  
        }           });
 rrord:', eion faile initializat Maple.error('❌conso              {
  r) rro } catch (e            
           ;
    fully') successzeditialiog('✅ Map inole.l        cons      
              );
    addTo(map }).           om: 18
       maxZo               tors',
  Map contribuenStreettion: '© Optribu     at            
   , {ng'.p{x}/{y}ap.org/{z}/treetm}.tile.opensttps://{sileLayer('h       L.t             
       , 2);
     ew([20, 0]Viap').setp('m= L.ma map       {
         try           
              map...');
ializing '🗺️ Initlog(console.          
  izeMap() {nitialfunction i
        
     });!');
   uccessfullyized sialboard init✅ Dashg('onsole.lo      c     );
 onality(unctirchF   setupSea       
  p();ializeMait          in...');
  boardDashing 🚀 Initializg('ole.lons          co  nction() {
ed', fuLoadentOMConter('DistenddEventL document.a
       icationpplalize the aIniti
        // );
).sort(tesdinaorntryCoct.keys(couObjees = tri const coun  st
      lie countries// Availabl

          };
      co2: 12000 }ess: 40.9, cc: 29.1549, a19.0154, lnge': { lat: -    'Zimbabw      },
   3, co2: 5000ccess: 37..8493, a39, lng: 27-13.13{ lat: a': 'Zambi            00 },
co2: 507.3,  access: 5g: 32.2903,ln 1.3733, : { lat:da'an  'Ug        
   },, co2: 29000s: 100.0cces 9.5375, alng:t: 33.8869, { la 'Tunisia':        
     11000 },: 37.7, co2:ss4.8888, acce: 3, lng6.3690 { lat: -a':    'Tanzani
        }, 17000 .0, co2:ccess: 60.2176, a8, lng: 30t: 12.862an': { laud         'S
   0 },co2: 1000.8, , access: 6814.4524: -74, lng: 14.49: { lat'Senegal'        },
     00089.3, co2: 1access: 29.8739, g: 9403, ln-1.t: la'Rwanda': {             2: 2000 },
 co 18.4,access:817, ng: 8.07.6078, l 1er': { lat:      'Nig
       4000 },2:: 56.0, coess acc04,, lng: 18.49 -22.9576lat:a': { amibi         'N
   , }004, co2: 80cess: 30.5296, acng: 35.18.6657, lt: -{ laue': ozambiq 'M
           o2: 3000 },, ccess: 50.49962, ac, lng: -3.lat: 17.5707'Mali': {      },
       2: 4000 .6, coccess: 26691, a lng: 46.8t: -18.7669,': { la 'Madagascar
           , 50000 }2:.0, coaccess: 70g: 17.2283,  ln1, lat: 26.335'Libya': {          000 },
  , co2: 11ss: 70.4cce5471, a-5.: 400, lng.5t': { lat: 7ry Coas        'Ivo
    2: 3000 },1, coss: 19.7, acce.758: 21ng -4.0383, l { lat:of Congo':lic ubcratic Rep   'Demo        ,
  }000: 8co2s: 62.1, ces12.3547, ac3697, lng: at: 7.': { lonero       'Cam },
      6000co2:0.3, cess: 74.6849, ac85, lng: 2.32 lat: -22: {tswana'     'Bo     
   },co2: 34000.0,  access: 438739,17.2027, lng:  -11.at:a': { lngol 'A         es
  an Countriricditional Af Ad         // 
              282000 },
9.0, co2:  access: 9108.2772,lng:  14.0583, am': { lat:  'Vietn
           156000 },0, co2: access: 99.897,.538, lng: -66at: 6.42': { luelaez   'Ven
         ountries/ V C   /       
            14000 },
   co2: 1cess: 100.0, 64.5853, acng:.3775, l lat: 41kistan': {'Uzbe          0 },
  co2: 70099.7, ess: 658, acc: -55.7lng -32.5228, ay': { lat:rugu        'U    ,
00 }co2: 54160.0, s: 100es795, acc.598 lng: -83,t: 39.82la { ':tates   'United S         000 },
.0, co2: 351000, access: 1 -3.436, lng:781at: 55.3 { l Kingdom':nited     'U,
       0 }co2: 20000.0, access: 10078,  lng: 53.84241,: 23.4lattes': { d Arab Emira 'Unite          02000 },
 .0, co2: 2ss: 10056, acce: 31.16lng: 48.3794, ': { lat  'Ukraine
          triesU Coun/           /     
    0 },
      35300, co2:ss: 100.0 acce33,g: 35.24.9637, lnat: 38rkey': { l   'Tu       
   43000 },: 99.9, co2:, access61.22258, lng: - 10.691o': { lat: and Tobag  'Trinidad         
  273000 },.8, co2:: 999925, access00.g: 15.8700, lnd': { lat: 1  'Thailan        ountries
  / T C      /  
               
  },38000.0, co2:  100s:.2275, acces182, lng: 86.8at: 4': { lerland   'Switz
         2: 35000 },s: 100.0, cocces.6435, ag: 18ln: 60.1282, : { lateden'    'Sw         23000 },
0, co2:100.cess: 8, aclng: 80.7711, lat: 7.873 Lanka': {  'Sri    ,
        }58000 2, co2:100.0access: .7492, ng: -3 40.4637, l{ lat:  'Spain':       },
    2: 611000 0.0, cocess: 10, ac: 127.7669ng5.9078, l: 3a': { latuth Kore   'So    0 },
     , co2: 45600.2ess: 84375, acc lng: 22.95595,t: -30.ca': { lari  'South Af  ,
        14000 } co2: .0,cess: 100 ac 14.9955,lng:.1512, 46lat: venia': {     'Slo      
  0 },000.0, co2: 3210access: .6990, , lng: 19.6690: { lat: 48ovakia'        'Sl  
  2: 37000 },00.0, co 18, access: 103.819, lng:at: 1.3521pore': { l     'Singa   ,
     1000 }100.0, co2:cess:  55.4920, ac.6796, lng:t: -4lles': { layche'Se       0 },
     0000, co2: 500.ccess: 1 a1.0059,lng: 2 44.0165, ': { lat:     'Serbia
       000 },2: 517s: 100.0, co92, acces 45.0759, lng: lat: 23.88rabia': {udi A       'Sa
     untries Co     // S   
         },
       0  co2: 17110000.0,access: 1, 5.31880, lng: 10: 61.524a': { lat   'Russi       },
   69000co2: : 100.0, 8, accessng: 24.966.9432, l: 45atania': { l   'Roms
          Countrie  // R           
          
 ,2: 103000 }100.0, co access: 39,ng: 51.18 25.3548, lr': { lat:  'Qata    es
      // Q Countri                  
   ,
   00 }80 co2: 40.0,cess: 108.2245, ac999, lng: -at: 39.3 ll': {tuga      'Por
      41000 }, 32:cos: 100.0, 1451, acces lng: 19.: 51.9194,nd': { lat'Pola       
     },00  12204.8, co2:ss: 9.7740, accelng: 12197, .87 { lat: 12hilippines':       'P,
     2: 57000 }co95.5, 52, access:  lng: -75.01at: -9.1900, 'Peru': { l          },
   co2: 700099.7,cess: 4438, ac lng: -58.: -23.4425,guay': { lat       'Para
      }, co2: 11000s: 91.8,escc.7821, a80ng: -: 8.5380, l lat'Panama': {     
        201000 },: 73.1, co2:51, access lng: 69.340.3753, { lat: 3stan':ki     'Paes
       untri    // P Co             
 },
        68000100.0, co2:4, access:  lng: 55.9755,47321. lat: 'Oman': {            
tries   // O Coun         
    
        2: 35000 },0.0, coaccess: 10, 468920, lng: 8.{ lat: 60.47':    'Norway      00 },
   2: 280 26.0, coccess:7.5101, a, lng: 120.3399: 4a': { latth Kore  'Nor
          2: 104000 },2.0, co, access: 6g: 8.6753 9.0820, lnria': { lat:   'Nige,
          }2: 37000.0, co: 1000, accessg: 174.88606, ln -40.90d': { lat:New Zealan   '
         2000 }, co2: 160,access: 100.2913, lng: 5.1326, t: 52.: { laetherlands'         'N000 },
    37, co2:cess: 90.0, ac.124 lng: 84 28.3949,l': { lat:'Nepa            ies
N Countr       //            
      0 },
2: 2100, co.1 access: 70: 95.9560,, lng21.9162': { lat: nmar      'Mya     00 },
 co2: 610ess: 99.4, 7.0926, acc17, lng: -: 31.79latcco': { 'Moro      0 },
      o2: 2400 90.0, c7, access:905g: 106. 47.0105, ln': { lat:golia       'Mon},
     o2: 486000 9.4, c: 9ess528, accg: -102.5 23.6345, lnico': { lat:   'Mex         : 5000 },
: 100.0, co2522, accesslng: 57.5 -20.3484, { lat:': ritiusMau '           0 },
: 200.0, co2cess: 10054, ac, lng: 14.37759335.lat:  'Malta': { 
            },: 2000o200.0, css: 107, acceng: 73.223.2028, llat: : { ives'       'Mald,
     254000 }o2: s: 99.8, ces8, accng: 101.9755, l210at: 4. { lia':lays     'Ma      tries
  // M Coun
                    0 },
    1000co2:ess: 100.0, acc: 6.1296, 3, lng.815: { lat: 49xembourg' 'Lu    
       4000 },o2: 10.0, caccess: 1023.8813, 694, lng: 5.1lat: 5': { nia    'Lithua        
 },2000 2co2:.0,  access: 100g: 35.8623, 33.8547, lnt:non': { la 'Leba        ,
    7000 }co2:0, 00.ss: 1.6032, acceg: 24.8796, lnat: 56 { la':Latvi     '},
       000 .0, co2: 17 access: 9555, 102.49g:.8563, ln19: { lat: 'Laos'        ies
    L Countr  //            
    
       0 },co2: 9200s: 100.0, acces8, 81 lng: 47.47,: 29.311 latwait': {        'Ku0 },
     1700 co2:s: 71.4,es acc: 37.9062,lng6, t: -0.023 { laya':en  'K
           },67000.0, co2: 2ccess: 100, a237, lng: 66.9t: 48.0196an': { lazakhst      'Kaies
      tr // K Coun       
                3000 },
.0, co2: 2access: 10036.2384, .5852, lng:  30: { lat:Jordan'     '     },
  000 622: 110.0, co: 10ccess138.2529, a, lng: : 36.2048{ lat: an'     'Jap     
  00 },.8, co2: 90cess: 985, ac97.2lng: -771096, { lat: 18.a':     'Jamaic        ntries
ou      // J C             
 000 },
    , co2: 335ss: 100.0ce ac674,, lng: 12.5lat: 41.8719ly': { ta    'I    ,
    00 }650: .0, co21006, access:  34.851, lng:lat: 31.0461l': {      'Israe   
    37000 },100.0, co2: ccess: .2439, a: -8ng l4129, 53.and': { lat:   'Irel          190000 },
 100.0, co2:ccess:, a3.679332, lng: 43.22: { lat: 3Iraq'     '
       00 },2: 6720co100.0, s: 880, acces3.6ng: 532.4279, l: { lat: 'Iran'       ,
     00 }6150o2: : 97.8, c, access.92133, lng: 1130.789 -a': { lat:'Indonesi       
     },00 2: 2654095.2, cocess: 9, acng: 78.9627, l: 20.593{ lat:  'India'          2000 },
 :  co200.0,: 108, access: -19.0264.9631, lngt: eland': { laIc       '  
   iesountr  // I C            
       ,
   0 }0, co2: 4800ccess: 100.: 19.5033, a7.1625, lng: { lat: 4  'Hungary'    
      iesuntr  // H Co               
  ,
     00 }co2: 670s: 100.0, .8243, acces742, lng: 219.0 3ce': { lat:   'Gree         00 },
 co2: 160s: 85.0,acces-1.0232, 9465, lng: lat: 7. 'Ghana': {   
          },o2: 729000.0, c 100cess:5, ac10.4517, lng: t: 51.165': { la    'Germany       
 2: 10000 },co100.0, cess: .3569, ac 43lng:154, .342a': { lat:    'Georgi     
    untries// G Co            
  
           }, co2: 330000: 100.0,83, access lng: 1.88.6034,: 46ance': { lat'Fr        },
     00co2: 450s: 100.0, ces25.7482, ac, lng: .9241t: 61la{ ': nd     'Finlaes
        Countri   // F
                 
    14000 },3, co2: ss: 44.7, acce0.489 4ng:1450, l: { lat: 9.ia'iop  'Eth         ,
 00 }160:  100.0, co2136, access: 25.0 lng:3,.595: { lat: 58 'Estonia'      
     : 234000 }, co2.6, access: 998025,30., lng: : 26.8206 { latt':  'Egyp
          2: 38000 }, co.2, access: 974,: -78.183.8312, lng lat: -1dor': {  'Ecua  s
        trieE Coun     //       
        
     : 22000 },o2: 98.1, c1627, access7, lng: -70.8.735: { lat: 1epublic'n Rminica       'Do
     0 },100 co2: 3ess: 100.0,.5018, acc, lng: 956.2639': { lat: 'Denmark       s
     ntrie    // D Cou         
     
      0 },co2: 10700ss: 100.0, acce.4730, 15 lng: : 49.8175,c': { lat Republiech       'Cz     2: 7000 },
 co0.0,ess: 10.4299, acc4, lng: 3335.126': { lat:     'Cyprus        0 },
0, co2: 26000.access: 10, : -77.7812 lngt: 21.5218,Cuba': { la    ',
        18000 }, co2: ss: 100.00, acce5.200 lng: 11000,5.a': { lat: 4 'Croati           2: 8000 },
: 99.7, cocess3.7534, ac lng: -8.7489,: 9: { lat Rica'   'Costa      
   4000 },.4, co2: 8s: 97cces74.2973, a09, lng: -.57lat: 4 { ombia':    'Col    000 },
    , co2: 10065: 100.0ess acc: 104.1954,35.8617, lngat:  lina': {'Ch    },
         co2: 87000 99.8,ccess: 0, a: -71.5431, lng35.675 lat: -hile': {'C           },
 00 72000.0, co2: 6, access: 13468106.g: -304, ln: 56.1ada': { lat     'Can
        10000 },: 89.1, co2:ccess04.9910, a657, lng: 112.5ia': { lat: mbod     'Ca       
riesC Count//         
             1000 },
   , co2: 400.0access: 158, : 25.48.7339, lnglat: 42aria': { ulg'B    
        0 },, co2: 1000ccess: 100.0 114.7277, a3, lng: 4.535lat:nei': { Bru      '0 },
      co2: 462009.7, cess: 953, aclng: -51.92-14.2350, lat:  { Brazil':    '
        },2: 25000  100.0, coss:791, acce: 17.6.9159, lngt: 43la: { ina'zegovnd Hera a     'Bosni       1000 },
3.0, co2: 2: 9ess, acc87lng: -63.58.2902,  -16 { lat:Bolivia':    '    000 },
    co2: 200.0, ss: 16, acce.43342, lng: 90: 27.51 latan': {      'Bhut  00 },
    0, co2: 1140access: 100., 4.4699lng: , at: 50.5039{ l'Belgium':         0 },
    00, co2: 580.0cess: 10 27.9534, ac098, lng:53.7{ lat: ': larus     'Be},
       4000 2.2, co2: 83, access: 9 lng: 90.356: 23.6850,esh': { lat 'Banglad        
   00 }, co2: 230ess: 100.0,, acc: 50.6378.9304, lng': { lat: 25hrainBa           's
 ntrie  // B Cou
                0 },
      37000.0, co2: s: 10 accesng: 47.5769,, l431t: 40.1{ la: n'  'Azerbaija    
       },20000.0, co2: 7ccess: 104.5501, a62, lng: 1{ lat: 47.51stria':   'Au       ,
   415000 } co2: : 100.0,, accessng: 133.7751744, l-25.2{ lat: a': rali   'Aust      ,
    5200 }00.0, co2:2, access: 145.038: 1, lng.069: 40: { lata'rmeni      'A},
      00 o2: 20102, css: 99..6167, acceng: -63 l161,: -38.4': { lat  'Argentina   },
       o2: 150000 : 99.4, c, accesslng: 1.6596: 28.0339, ria': { latlge  'A
          : 4500 },0, co2ess: 100.20.1683, acc533, lng: lat: 41.1: { Albania'  '