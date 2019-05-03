#NEXUS

BEGIN TAXA;
    DIMENSIONS NTAX=17;
    TAXLABELS
        'Kentropyx_calcarata'
        'Typhlops_brongersmianus'
        'Brasiliscincus_heathi'
        'Copeoglossum_nigropunctatum'
        'Notomabuya_frenata'
        'Ameivula_mumbuca'
        'Hemidactylus_mabouia'
        'Gymnodactylus_amarali'
        'Colobosaura_modesta'
        'Outgroup_outgroup'
        'Anolis_meridionalis'
        'Anolis_brasiliensis'
        'Amphisbaena_alba'
        'Tantilla_melanocephala'
        'Tropidurus_oreadicus'
        'Bothrops_moojeni'
        'Micrablepharus_maximiliani'
  ;
END;

BEGIN TREES;
    TREE 1 = ('Kentropyx_calcarata':1e-06,('Typhlops_brongersmianus':0.0041921882,('Brasiliscincus_heathi':1e-06,'Copeoglossum_nigropunctatum':1e-06,'Notomabuya_frenata':1e-06):0.0027311228):0.0027807459,'Ameivula_mumbuca':1e-06,'Hemidactylus_mabouia':2.2834e-06,(('Gymnodactylus_amarali':0.0013502231,'Colobosaura_modesta':0.0139415601):0.001314644,'Outgroup_outgroup':0.0054901158):0.0027693122,((('Anolis_meridionalis':1e-06,'Anolis_brasiliensis':1e-06):0.0127263226,'Amphisbaena_alba':0.0013609777):0.0014448824,'Tantilla_melanocephala':0.010038587):0.0013123595,'Tropidurus_oreadicus':0.004106912,'Bothrops_moojeni':0.0013607322,'Micrablepharus_maximiliani':0.0027387161);
    TREE 2 = ('Kentropyx_calcarata':2.2834e-06,(('Typhlops_brongersmianus':0.0026504524,('Anolis_meridionalis':2.2834e-06,'Anolis_brasiliensis':2.2834e-06):0.0054077058,'Amphisbaena_alba':0.0013303694,'Tantilla_melanocephala':0.0013234409):0.0026409065,'Bothrops_moojeni':2.0227e-06,'Tropidurus_oreadicus':0.001310758):0.0013183499,'Ameivula_mumbuca':2.2834e-06,'Gymnodactylus_amarali':0.0026186365,'Hemidactylus_mabouia':2.2834e-06,('Brasiliscincus_heathi':2.2834e-06,'Copeoglossum_nigropunctatum':2.2834e-06,'Notomabuya_frenata':2.2834e-06):0.0026289676,'Outgroup_outgroup':0.0026211098,('Colobosaura_modesta':0.0066921853,'Micrablepharus_maximiliani':0.0068794099):0.0027415078);
    TREE 3 = ('Kentropyx_calcarata':2.2834e-06,(('Typhlops_brongersmianus':0.0013927816,'Tantilla_melanocephala':0.0029623343):0.0013830124,'Bothrops_moojeni':2.0735e-06):0.0013767017,'Ameivula_mumbuca':2.2834e-06,'Hemidactylus_mabouia':2.2786e-06,('Gymnodactylus_amarali':0.0070850433,'Outgroup_outgroup':0.0041464965):0.0013641176,('Colobosaura_modesta':0.015921497,'Micrablepharus_maximiliani':0.0041151089):0.0042894785,('Brasiliscincus_heathi':2.2834e-06,'Notomabuya_frenata':2.3562e-06,'Copeoglossum_nigropunctatum':2.14e-06):0.0027567031,((('Anolis_meridionalis':2.2834e-06,'Anolis_brasiliensis':2.2834e-06):0.0128095672,'Tropidurus_oreadicus':0.0027938718):0.0028195317,'Amphisbaena_alba':0.0099335806):0.0014291827);
    TREE 4 = ('Kentropyx_calcarata':2.2834e-06,('Typhlops_brongersmianus':0.0026967912,'Brasiliscincus_heathi':2.2834e-06,'Copeoglossum_nigropunctatum':2.2834e-06,'Notomabuya_frenata':2.2834e-06):0.0013369206,'Ameivula_mumbuca':2.2834e-06,('Bothrops_moojeni':2.1453e-06,'Tantilla_melanocephala':2.0028e-06):0.0013382824,'Hemidactylus_mabouia':2.2834e-06,('Gymnodactylus_amarali':0.0055151079,'Colobosaura_modesta':0.0068323085):0.0026760792,'Tropidurus_oreadicus':0.0013356813,('Anolis_meridionalis':2.2834e-06,'Anolis_brasiliensis':2.2834e-06):0.0068399685,'Micrablepharus_maximiliani':0.0026821299,'Outgroup_outgroup':0.0067693507,'Amphisbaena_alba':0.0040553428);
    TREE 5 = ('Kentropyx_calcarata':1e-06,((('Typhlops_brongersmianus':0.0027379139,('Anolis_meridionalis':1e-06,'Anolis_brasiliensis':1e-06):0.0097613278,'Tantilla_melanocephala':0.0070168434):0.002712611,'Bothrops_moojeni':2.2942e-06):0.0013152355,'Tropidurus_oreadicus':0.0054572027):0.0041614258,'Ameivula_mumbuca':1e-06,'Hemidactylus_mabouia':2.2834e-06,('Gymnodactylus_amarali':0.0082211888,'Colobosaura_modesta':0.01681152,'Outgroup_outgroup':0.0040337693):0.00270651,'Micrablepharus_maximiliani':0.0098408629,'Amphisbaena_alba':0.0083330565,('Brasiliscincus_heathi':1e-06,'Notomabuya_frenata':1e-06,'Copeoglossum_nigropunctatum':1e-06):0.0040747199);
    TREE 6 = ('Kentropyx_calcarata':2.2834e-06,(('Typhlops_brongersmianus':2.2834e-06,'Bothrops_moojeni':0.001353437,'Tantilla_melanocephala':0.001359217):0.0013439232,(('Anolis_meridionalis':2.2834e-06,'Anolis_brasiliensis':2.2834e-06):0.0097659933,'Tropidurus_oreadicus':0.0033330106):0.002143277):0.0013644766,'Ameivula_mumbuca':2.2834e-06,('Hemidactylus_mabouia':2.2834e-06,'Brasiliscincus_heathi':2.2834e-06,'Copeoglossum_nigropunctatum':2.2834e-06,'Notomabuya_frenata':2.2834e-06):0.0013435689,(('Gymnodactylus_amarali':0.0085290535,'Colobosaura_modesta':0.012734824):0.0025994243,'Outgroup_outgroup':0.0097110419):0.0013461639,'Amphisbaena_alba':0.0041394308,'Micrablepharus_maximiliani':0.0040907455);
    TREE 7 = ('Kentropyx_calcarata':2.2834e-06,((('Typhlops_brongersmianus':0.0028037523,'Tantilla_melanocephala':0.0057014655):0.0013353828,'Bothrops_moojeni':0.0027731308):0.0027368825,(('Anolis_meridionalis':2.2834e-06,'Anolis_brasiliensis':2.2834e-06):0.0111748452,'Tropidurus_oreadicus':0.0031019582):0.0023948697):0.0013742225,'Ameivula_mumbuca':2.2834e-06,'Hemidactylus_mabouia':2.2834e-06,('Gymnodactylus_amarali':2.2483e-06,'Colobosaura_modesta':0.0124587678):0.002706142,'Amphisbaena_alba':0.0070687397,'Outgroup_outgroup':0.0096384753,('Brasiliscincus_heathi':2.2834e-06,'Copeoglossum_nigropunctatum':2.2834e-06,'Notomabuya_frenata':2.2834e-06):0.001358164,'Micrablepharus_maximiliani':0.0083068756);
    TREE 8 = ('Kentropyx_calcarata':2.2834e-06,(('Typhlops_brongersmianus':0.0026762389,'Tantilla_melanocephala':0.0068340601,'Bothrops_moojeni':0.0013302092):0.0013210024,(('Anolis_meridionalis':2.2834e-06,'Anolis_brasiliensis':2.2834e-06):0.0040215295,'Tropidurus_oreadicus':0.0026690728):0.0013403015):0.0013388732,'Ameivula_mumbuca':2.2834e-06,'Amphisbaena_alba':2.2834e-06,('Gymnodactylus_amarali':0.0053771928,'Colobosaura_modesta':0.0094913853,'Outgroup_outgroup':0.0040338201):0.0013234562,'Hemidactylus_mabouia':2.2834e-06,'Micrablepharus_maximiliani':0.006735789,('Brasiliscincus_heathi':2.2834e-06,'Copeoglossum_nigropunctatum':2.2834e-06,'Notomabuya_frenata':2.2834e-06):0.0040183788);
    TREE 9 = ('Kentropyx_calcarata':1e-06,((('Typhlops_brongersmianus':0.0028395733,'Tantilla_melanocephala':0.0100657):0.0012619825,'Bothrops_moojeni':0.0013628955):0.0013434807,(('Anolis_meridionalis':1e-06,'Anolis_brasiliensis':1e-06):0.0082742049,'Tropidurus_oreadicus':2.0246e-06):0.0027176828):0.0013622237,'Ameivula_mumbuca':1e-06,'Brasiliscincus_heathi':2.2834e-06,'Notomabuya_frenata':1e-06,'Copeoglossum_nigropunctatum':1e-06,('Gymnodactylus_amarali':0.0027108086,'Colobosaura_modesta':0.0068169865):0.0041187007,'Amphisbaena_alba':0.0041271013,'Hemidactylus_mabouia':2.2834e-06,'Outgroup_outgroup':0.0123868533,'Micrablepharus_maximiliani':0.0082503501);
    TREE 10 = ('Kentropyx_calcarata':2.2834e-06,((('Typhlops_brongersmianus':0.0013572634,'Amphisbaena_alba':0.0057426838):0.0042511437,'Tantilla_melanocephala':0.0028253711):0.0013098885,'Bothrops_moojeni':2.0567e-06,(('Anolis_meridionalis':2.2834e-06,'Anolis_brasiliensis':2.2834e-06):0.0111411323,'Tropidurus_oreadicus':0.0014251509):0.0040534346):0.0013652476,'Ameivula_mumbuca':2.2834e-06,'Hemidactylus_mabouia':2.018e-06,('Gymnodactylus_amarali':0.0041126169,('Colobosaura_modesta':0.0126544158,'Micrablepharus_maximiliani':0.0085646118):0.0043200371,'Outgroup_outgroup':0.0082694519):0.0013111889,('Brasiliscincus_heathi':2.2834e-06,'Copeoglossum_nigropunctatum':2.2834e-06,'Notomabuya_frenata':2.1403e-06):0.0027218996);
END;

