from automata.automata_network import Automatanetwork
from automata.elemnts.ste import S_T_E, PackedIntervalSet, PackedInterval, PackedInput, get_Symbol_type
from automata.elemnts.element import StartType
from automata.utility.utility import minimize_automata

my_Automata = Automatanetwork(id="test1", is_homogenous=True, stride=1, max_val=255)

ste1 = S_T_E(start_type=StartType.start_of_data, is_report=False, is_marked=False, id = my_Automata.get_new_id(),
             symbol_set=get_Symbol_type(True)([PackedInterval(PackedInput((1, )), PackedInput((1,)))]),
             adjacent_S_T_E_s=None, report_residual=0, report_code=-1)

ste2 = S_T_E(start_type=StartType.start_of_data, is_report=False, is_marked=False, id = my_Automata.get_new_id(),
             symbol_set=get_Symbol_type(True)([PackedInterval(PackedInput((2,)), PackedInput((2,)))]),
             adjacent_S_T_E_s=None, report_residual=0, report_code=-1)

ste3 = S_T_E(start_type=StartType.non_start, is_report=False, is_marked=False, id = my_Automata.get_new_id(),
             symbol_set=PackedIntervalSet([PackedInterval(PackedInput((3,)), PackedInput((3,)))]),
             adjacent_S_T_E_s=None, report_residual=0, report_code=-1)

ste4 = S_T_E(start_type=StartType.non_start, is_report=False, is_marked=False, id = my_Automata.get_new_id(),
             symbol_set=get_Symbol_type(True)([PackedInterval(PackedInput((4,)), PackedInput((4,)))]),
             adjacent_S_T_E_s=None, report_residual=0, report_code=0)

ste5 = S_T_E(start_type=StartType.non_start, is_report=False, is_marked=False, id = my_Automata.get_new_id(),
             symbol_set=get_Symbol_type(True)([PackedInterval(PackedInput((5,)), PackedInput((5,)))]),
             adjacent_S_T_E_s=None, report_residual=0, report_code=-1)

ste6 = S_T_E(start_type=StartType.non_start, is_report=False, is_marked=False, id = my_Automata.get_new_id(),
             symbol_set=PackedIntervalSet([PackedInterval(PackedInput((6,)), PackedInput((6,)))]),
             adjacent_S_T_E_s=None, report_residual=0, report_code=-1)

ste7 = S_T_E(start_type=StartType.non_start, is_report=True, is_marked=False, id = my_Automata.get_new_id(),
             symbol_set=get_Symbol_type(True)([PackedInterval(PackedInput((7,)), PackedInput((7,)))]),
             adjacent_S_T_E_s=None, report_residual=0, report_code=0)

ste8 = S_T_E(start_type=StartType.start_of_data, is_report=False, is_marked=False, id = my_Automata.get_new_id(),
             symbol_set=get_Symbol_type(True)([PackedInterval(PackedInput((8,)), PackedInput((8,)))]),
             adjacent_S_T_E_s=None, report_residual=0, report_code=0)


hmh=True

my_Automata.add_element(ste1)
my_Automata.add_element(ste2)
my_Automata.add_element(ste3)
my_Automata.add_element(ste4)
my_Automata.add_element(ste5)
my_Automata.add_element(ste6)
my_Automata.add_element(ste7)
my_Automata.add_element(ste8)


my_Automata.add_edge(ste1, ste3)
my_Automata.add_edge(ste3, ste5)
my_Automata.add_edge(ste5, ste7)
my_Automata.add_edge(ste2, ste4)
my_Automata.add_edge(ste4, ste6)
my_Automata.add_edge(ste6, ste7)
my_Automata.add_edge(ste8, ste3)
my_Automata.add_edge(ste1, ste6)


my_Automata.draw_graph('t.svg')

my_Automata=my_Automata.get_single_stride_graph()
my_Automata.draw_graph('S2NH.svg')
if hmh:
    my_Automata.make_homogenous()
    my_Automata.draw_graph('S2H.svg')
my_Automata=my_Automata.get_single_stride_graph()

my_Automata.draw_graph('S2H2.svg' if hmh else 'S4.svg')

my_Automata.make_homogenous()

minimize_automata(my_Automata, combine_equal_syms_only=hmh)
my_Automata.draw_graph('S4Hwith_H.svg' if hmh else 'S4HNo_H.svg')
print my_Automata.get_summary()

for n in my_Automata.nodes:
    if n.start_type == StartType.fake_root:
        continue
    s = n.is_symbolset_splitable()
    if not s:
        print n.id