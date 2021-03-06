from acc import *
from var import *
import time
import numpy as np


# input transfer
def run_CA_on_peachtree(simitime,arr_time10,linkToGo_10,objDirection_10,arr_time11,arr_time12,arr_time13):
	# seperate car
	arr_timeL = []
	arr_timeR = []
	linkToGo_10L = []
	linkToGo_10R = []
	objDirection_10L = []
	objDirection_10R = []

	#change this
	# randomSeed = int(round(time.time() * 1000)) % 4294967296
	randomSeed = 1
	np.random.seed(randomSeed)

	for index in range(len(arr_time10)):
		if objDirection_10[index] == 1:
			arr_timeL.append(arr_time10[index])
			linkToGo_10L.append(linkToGo_10[index])
			objDirection_10L.append(objDirection_10[index])
		elif objDirection_10[index] == 2:
			arr_timeR.append(arr_time10[index])
			linkToGo_10R.append(linkToGo_10[index])
			objDirection_10R.append(objDirection_10[index])
		else:
			cho = np.random.choice([0, 1])
			if cho == 0:
				arr_timeL.append(arr_time10[index])
				linkToGo_10L.append(linkToGo_10[index])
				objDirection_10L.append(objDirection_10[index])
			else:
				arr_timeR.append(arr_time10[index])
				linkToGo_10R.append(linkToGo_10[index])
				objDirection_10R.append(objDirection_10[index])


	#transform datatype

	spawn_time_10th_L = []
	arr_timeL = [0] + arr_timeL
	for index in range(len(arr_timeL)):
		if index is not 0:
			spawn_time_10th_L.append(int(round(arr_timeL[index]-arr_timeL[index-1],0)))

	spawn_time_10th_R = []
	arr_timeR = [0] + arr_timeR
	for index in range(len(arr_timeR)):
		if index is not 0:
			spawn_time_10th_R.append(int(round(arr_timeR[index]-arr_timeR[index-1],0)))




	spawn_delay_10th_L = []
	for i in linkToGo_10L:
		spawn_delay_10th_L.append(i-1)
	spawn_delay_10th_R = []
	for i in linkToGo_10R:
		spawn_delay_10th_R.append(i - 1)

	spawn_comm_10th_L = []
	for i in objDirection_10L:
		table = {0:'D',1:'L',2:'R'}
		spawn_comm_10th_L.append(table[i])
	spawn_comm_10th_R = []
	for i in objDirection_10R:
		table = {0:'D',1:'L',2:'R'}
		spawn_comm_10th_R.append(table[i])


	spawn_time_11th = []
	arr_time11 = [0] + arr_time11
	for index in range(len(arr_time11)):
		if index is not 0:
			spawn_time_11th.append(int(round(arr_time11[index]-arr_time11[index-1],0)))
	if len(spawn_time_11th) == 0:
		spawn_time_11th = [9999999]
	spawn_comm_11th = ['D']*len(spawn_time_11th)
	spawn_delay_11th = [0]*len(spawn_time_11th)

	spawn_time_12th = []
	arr_time12 = [0] + arr_time12
	for index in range(len(arr_time12)):
		if index is not 0:
			spawn_time_12th.append(int(round(arr_time12[index]-arr_time12[index-1],0)))
	if len(spawn_time_12th) == 0:
		spawn_time_12th = [9999999]
	spawn_comm_12th = ['D']*len(spawn_time_12th)
	spawn_delay_12th = [0]*len(spawn_time_12th)

	spawn_time_13th = []
	arr_time13 = [0] + arr_time13
	for index in range(len(arr_time13)):
		if index is not 0:
			spawn_time_13th.append(int(round(arr_time13[index]-arr_time13[index-1],0)))
	if len(spawn_time_13th) == 0:
		spawn_time_13th = [9999999]
	spawn_comm_13th = ['D']*len(spawn_time_13th)
	spawn_delay_13th = [0]*len(spawn_time_13th)



	## map construction
	##def __init__(self, dir, spawn=None, spawnarray = None, spawncommarray = None, spawndelayarray = None, spawndir=None, trafficlight=None, trafficlight_stop=0, trafficlightinit = True):
	LLane = []
	RLane = []
	LLane.append(road(E,spawn=True,spawnarray=spawn_time_10th_L,spawndelayarray=spawn_delay_10th_L,spawncommarray=spawn_comm_10th_L,spawndir=1,spawnatorig = 1))  # 10th street init spawn point
	RLane.append(road(E,spawn=True,spawnarray=spawn_time_10th_R,spawndelayarray=spawn_delay_10th_R,spawncommarray=spawn_comm_10th_R,spawndir=1,spawnatorig = 1))  # 10th street init spawn point
	for i in range(19):
		LLane.append(road(E))
		RLane.append(road(E))

	LLane.append(road(NE)) #11th left turn lane
	RLane.append(road(E))

	for i in range(4):
		LLane.append(road(E))
		RLane.append(road(E))

	LLane.append(road(E,trafficlight=45, trafficlight_stop=65, trafficlightinit = True)) #11th traffic light
	RLane.append(road(E,trafficlight=45, trafficlight_stop=65, trafficlightinit = True))

	for i in range(4):
		LLane.append(road(E))
		RLane.append(road(E))

	LLane.append(road(E)) #11th right turn
	RLane.append(road(SE))

	LLane.append(road(E))
	RLane.append(road(E,spawn=True,spawnarray=spawn_time_11th,spawndelayarray=spawn_delay_11th,spawncommarray=spawn_comm_11th,spawndir=1)) #11th right turn enter spawn point

	for i in range(56):
		LLane.append(road(E))
		RLane.append(road(E))

	LLane.append(road(NE)) #12th left turn lane
	RLane.append(road(E))

	for i in range(28):
		LLane.append(road(E))
		RLane.append(road(E))

	LLane.append(road(E,trafficlight=65, trafficlight_stop=35, trafficlightinit = True)) #12th traffic light
	RLane.append(road(E,trafficlight=65, trafficlight_stop=35, trafficlightinit = True))

	LLane.append(road(E))
	RLane.append(road(SE))#12th right turn

	LLane.append(road(E))
	RLane.append(road(E,spawn=True,spawnarray=spawn_time_12th,spawndelayarray=spawn_delay_12th,spawncommarray=spawn_comm_12th,spawndir=1)) #12th right turn enter spawn point

	for i in range(80):
		LLane.append(road(E))
		RLane.append(road(E))

	LLane.append(road(E))
	RLane.append(road(SE)) #13th right turn

	LLane.append(road(E))
	RLane.append(road(E, spawn=True, spawnarray=spawn_time_13th, spawndelayarray=spawn_delay_13th,spawncommarray=spawn_comm_13th, spawndir=1)) #13th right turn enter spawn point

	for i in range(20):
		LLane.append(road(E))
		RLane.append(road(E))

	LLane.append(road(E,trafficlight=50, trafficlight_stop=50, trafficlightinit = True))  #14th traffic light
	RLane.append(road(E,trafficlight=50, trafficlight_stop=50, trafficlightinit = True))

	localmap = [LLane,RLane]





	#
	#
	# localmap = []
	# localmap.append(road(E, spawn=1, spawndir=1, spawnarray=[2,1,2,1],spawncommarray=['D','R','D','R'],spawndelayarray=[0,1,0,1]))
	# for i in range(30):
	# 	localmap.append(road(E))
	# localmap.append(road(E,trafficlight=10, trafficlight_stop=10, trafficlightinit = False))
	# localmap.append(road(SE))#
	# for i in range(30):
	# 	localmap.append(road(E))
	# localmap.append(road(SE))#
	# for i in range(30):
	# 	localmap.append(road(E))
	# localmap = [localmap]
	#
	#
	# game = map(localmap)

	#
	# game.put_car(0,0,car('D',0,1,0))
	# game.put_car(0,1,car('R',0,1,0))
	# game.put_car(0,2,car('D',0,1,0))
	# game.put_car(0,1,car('D',0,1,0))
	# game.put_car(0,2,car('D',0,1,0))
	game = map(localmap)
	TravelTimeList = []
	Time_log = []
	for i in range(simitime):
		#print(i, end= ':')
		#print(game)

		#print(str(game.main_exit_time_count) +'/' + str(game.main_exit_veh_count))

		game.update()
		if game.main_exit_veh_count != 0:
			TravelTimeList.append(game.main_exit_time_count / game.main_exit_veh_count)
			Time_log.append(game.systime)

		#time.sleep(0.2)

	if game.speedcount != 0:
		print('average speed %.2f'%(game.speedsum / game.speedcount), end=', ')
	if game.main_exit_veh_count != 0:
		print('average time travel through %.2f'%(game.main_exit_time_count / game.main_exit_veh_count))

	return[[TravelTimeList,Time_log],game.main_exit_veh_count,(game.speedsum / game.speedcount),(game.main_exit_time_count / game.main_exit_veh_count)]

if __name__ == '__main__':
	simtime = 1800
	arr_time10 = [18.797498865099353, 20.493645893452225, 22.349362381005495, 23.382122899556215, 44.780369533259844, 46.22462798802667, 62.01192695279525, 62.369054877110706, 73.45871901553326, 74.46199914769159, 77.18284442239349, 78.45678447169993, 79.45927933356573, 90.68039097507965, 99.31233308742063, 100.88211996832442, 103.33743933469775, 109.13202411971658, 110.69600476300147, 112.01548637768633, 113.00014245097371, 117.21486071913932, 119.87949335791531, 121.14011424426846, 124.59944972374575, 126.25016632238422, 129.97744087364183, 136.33945772150804, 140.8630874072478, 143.10540342624327, 145.72158608612648, 151.8777310315144, 156.3309528473705, 164.81820421423686, 170.50518298007344, 172.88200835614367, 183.94617292408364, 200.74456101860784, 235.12323562323118, 235.8524540476437, 239.7430953133413, 248.14882683284665, 252.74833753727137, 253.1203418290507, 257.31551537637165, 264.7498927217838, 267.3285413126048, 269.9677213860303, 274.0218385749946, 277.74450392463484, 281.4784493588669, 292.517108576202, 294.70454551689687, 296.3521846277535, 298.61484435543036, 302.0474505023793, 304.07220540888613, 316.29888304054697, 317.307551501523, 321.2375017222782, 328.5022676296775, 329.676402274558, 330.4241921402981, 335.021350554852, 339.79687389656914, 340.59523481338266, 343.73704226296235, 344.3130373228995, 347.50278715628986, 348.9255277145788, 349.36940822560155, 361.7503571295647, 362.65192101451134, 370.9424974817554, 371.81468995871285, 377.73644900820165, 385.421227937908, 387.0960277554288, 394.8560184542644, 398.29961031737326, 406.6397482958415, 413.9819389815968, 419.77097797886773, 423.56925447638775, 427.77527176929806, 434.60059916548164, 444.61357443736284, 479.044218477937, 484.3098262825422, 487.25063996928606, 490.5878998056386, 491.5675814172566, 493.445542510993, 494.5662112304643, 500.1458242787317, 502.86001936145016, 537.4287197081817, 537.8546480953145, 587.5609339006975, 590.0676348629615, 603.7850369366561, 606.1895972549726, 607.022812832473, 611.6120082059167, 614.5204441830624, 616.2063942660417, 620.6360992981292, 623.6637162765473, 649.0765833271108, 659.898587878361, 666.159556927753, 671.3070947675279, 673.4351318069115, 681.3821911596501, 682.1638385398671, 682.6566927326363, 683.6394387698621, 710.497556049313, 712.8028513986206, 713.575533590314, 714.4413739245788, 722.8441221702074, 737.7314038551463, 741.4947060942667, 759.0126010932817, 762.6969979136707, 764.5179072814732, 767.1625443656594, 771.4148496823507, 775.4843924586189, 778.3616558854981, 779.2309797178164, 779.7718898979056, 787.7277096191584, 789.644202242002, 791.9882932605088, 793.2851049626394, 800.0531141869535, 823.0189355181004, 823.8229470057636, 823.9852831550728, 850.3127785814402, 880.0637225549282, 886.2135056509063, 889.88532085269, 890.5199308822944, 898.2230769389856, 900.4125069240066, 904.8617104561862, 909.205546710998, 917.2558466183981, 934.4850751521326, 941.8938616939107, 950.3789920422875, 951.0742161689624, 963.4031878115846, 964.815635246823, 966.8614505684823, 970.3579823290016, 974.4684170185222, 975.4539635642252, 979.0272143207847, 984.5895997638945, 986.164544893894, 991.2956072500824, 998.9142412610917, 1029.1364378523672, 1029.8093812683253, 1031.1503746598737, 1032.4205938640023, 1035.743322267549, 1037.2947010500388, 1048.2614978588554, 1052.8099965405008, 1138.155022263208, 1146.1070328625754, 1152.7300548408928, 1155.8299232371457, 1158.6595721462486, 1160.0488767368633, 1166.4374994046536, 1175.5981632203068, 1178.1338633211822, 1189.4832171249368, 1190.6038943216495, 1193.5237816520676, 1209.1307694491352, 1210.8154962089288, 1211.0364627324902, 1211.373428559964, 1213.4088823740176, 1218.0476083535561, 1220.9574698667775, 1224.2630728487825, 1226.9963248422268, 1229.7120467909813, 1239.420646774804, 1248.2323608527217, 1249.7726802623033, 1251.610416403554, 1253.6316688900051, 1255.2206190436398, 1255.6255651128895, 1260.4111078253363, 1266.1112162880736, 1266.2754053107412, 1272.4184749724648, 1277.060929322782, 1285.2622368997154, 1287.362639570427, 1320.0201497648425, 1321.4271042971607, 1321.9224900843153, 1328.9886613477, 1329.6143827103936, 1331.6374685918488, 1334.528629440133, 1337.2406187240995, 1337.9466354207732, 1359.884396076517, 1360.9754943049825, 1368.6745161218284, 1371.8275897205, 1403.542634826989, 1408.4046473227604, 1420.7421909495226, 1422.82050604193, 1426.4151042187777, 1426.7419656492423, 1428.0829634134388, 1433.406959051442, 1444.1491405014126, 1465.9056933851061, 1468.9741638825212, 1470.392782520997, 1481.270626818225, 1485.843681218797, 1486.187943973675, 1488.3765112723734, 1489.8383337140924, 1491.7945178571215, 1496.5680955944013, 1508.5854747193807, 1519.4616890947395, 1530.7091049709418, 1533.8139319787367, 1541.6324347163718, 1564.0905915362155, 1565.0308815654557, 1579.0262528984122, 1580.3368932428548, 1589.9494138006107, 1591.7970389364946, 1602.7017389703951, 1613.3842533931327, 1614.6260245154317, 1616.297564368541, 1618.0267119001787, 1628.106362643485, 1634.4091965378482, 1639.7248348177854, 1661.6007407617435, 1669.1593648364385, 1672.0418742122624, 1674.1289693916137, 1676.0850950027468, 1681.4062679115475, 1682.9572674097897, 1684.3920755217503, 1691.1590596187004, 1703.0398646381952, 1723.5321215346617, 1726.4565644547088, 1732.9081213498575, 1735.0044213776462, 1740.3303077575856, 1746.1157013617383, 1746.4109312243559, 1746.9261714436293, 1750.4090796555492, 1752.8880323060025, 1756.9030617420942, 1758.6890248766533, 1762.2961031564357, 1782.5519941414311, 1786.599880158123, 1793.5050733281994, 1794.9542176126272, 1798.9337542940655]
	linkToGo_10 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 4, 2, 4, 4, 1, 4, 4, 4, 1, 2, 2, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 4, 1, 4, 4, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 4, 4, 4, 2, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 1, 4, 4, 2, 2, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 1, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 4, 4, 4, 4, 1, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 1, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 4, 4]
	objDirection_10 = [2, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 2, 0, 1, 0, 2, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 2, 0, 0, 2, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 2, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 2, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 2, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 2, 2, 0, 0, 0, 0, 2, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 2, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
	#0 straight, 1 left turn, 2 right turn

	arr_time11 = [299.5018955494773, 786.5226405166106, 1170.9712812415319, 1527.4573625357843]
	arr_time12 = [12.542903007976642, 157.11765555441397, 819.3709502178715]
	arr_time13 = [14.844518493747355, 43.646132775762, 105.12604352190051, 132.67100084227974, 157.0304815073447, 245.16239190888547, 270.66619859784385, 275.25758173358787, 335.2229579987889, 358.64934840823037, 374.879384827311, 380.86730701759114, 511.5884599607788, 514.3045963710255, 519.4087733262126, 547.3901472054287, 716.4432410577346, 902.6267599735513, 912.410445617737, 943.8772475609125, 950.2742032499177, 1080.5873384966992, 1087.2487740384304, 1120.0378239413544, 1253.7874738072135, 1283.6142292635332, 1509.1598323112992, 1522.9140183767777, 1583.4080390719867, 1691.3047428114642, 1724.2306243564396]

	run_CA_on_peachtree(simtime, arr_time10, linkToGo_10, objDirection_10, arr_time11, arr_time12, arr_time13)
