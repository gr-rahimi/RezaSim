import automata as atma
from automata.AnmalZoo.anml_zoo import anml_path,input_path,AnmalZoo
from tqdm import tqdm
tqdm.monitor_interval = 0

for automata_name, automata_path in anml_path.iteritems():
    if automata_name != AnmalZoo.Levenshtein:
        continue
    automata = atma.parse_anml_file(automata_path)
    print "Finished processing from anml file. Here is the summary", str(automata_name)

    automata.remove_ors()

    #automata.re_label_automata_states(4)

    orig_automatas = automata.get_connected_components_as_automatas()

    for orig_cc_idx, orig_cc in tqdm(enumerate(orig_automatas), unit="automata"):
        print "Start processing CC", orig_cc_idx
        orig_cc.remove_all_start_nodes()
        #minimize_automata(orig_cc)
        orig_cc.print_summary(logo="O")
        orig_cc.draw_graph("O.svg", use_dot= True)
        #print orig_cc.get_number_of_start_nodes()
        fst_st_atm = orig_cc.get_single_stride_graph()
        #fst_st_atm.make_homogenous()
        #minimize_automata(automata, merge_reports = True, same_residuals_only = False, same_report_code = False)
        fst_st_atm.print_summary(logo="HS")
        fst_st_atm.draw_graph("HS.svg", use_dot=True)
        fst_st_atm = fst_st_atm.get_single_stride_graph()
        #fst_st_atm = fst_st_atm.get_single_stride_graph()
        #fst_st_atm = fst_st_atm.get_single_stride_graph()
        #fst_st_atm = orig_cc.get_single_stride_graph()
        #fst_st_atm = fst_st_atm.get_single_stride_graph()
        #fst_st_atm = fst_st_atm.get_single_stride_graph()
        #fst_st_atm = fst_st_atm.get_single_stride_graph()
        fst_st_atm.print_summary(logo = "HSS")
        fst_st_atm.draw_graph("HSS.svg", use_dot=True)
        #fst_st_atm.draw_graph("nonhomo_fst.svg",use_dot= True)

        #fst_st_atm.make_homogenous()
        #fst_st_atm.print_summary(logo="SH")
        #fst_st_atm.draw_graph("homo_fst.svg", use_dot=True)


        #minimize_automata(fst_st_atm,merge_reports= True, same_residuals_only= True, same_report_code = True)


        #fst_st_atm.draw_graph("homo_fst_minimized.svg", use_dot=True)
        #fst_st_atm.print_summary(logo="OSSHM")

        #atma.compare_input(True, True, input_path[automata_name], orig_cc, fst_st_atm)

        #false_stat_per_state = atma.compare_real_approximate(input_path[automata_name], fst_st_atm)

        #final_nodes = fst_st_atm.get_filtered_nodes(lambda node: node.is_report())
        #for fn in final_nodes:
        #    fst_st_atm._make_homogeneous_STE(fn, delete_original_ste=True)

        #sorted_false_stat = sorted(false_stat_per_state.iteritems(), key=lambda (k, v): (v, k))
        #for i in range(20):
        #    fst_st_atm._make_homogeneous_STE(sorted_false_stat[i][0], delete_original_ste = True)


        #fst_st_atm.print_summary(logo="OSSHMsh")
        atma.compare_real_approximate(input_path[automata_name], fst_st_atm)

        break





        #frt_st_atm = thd_st_atm.get_single_stride_graph()

        #frt_st_atm.make_homogenous()

        #print "fourth stride automata:"
        #frt_st_atm.print_summary()
        #minimize_automata(frt_st_atm)

        #print max([cc.get_number_of_nodes(True) for cc in frt_st_atm.get_connected_components_as_automatas()])






















