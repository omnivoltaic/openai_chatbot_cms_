from langchain.llms import OpenAI
llm = OpenAI(temperature=0, openai_api_key="openai_api_keys")
context = """Omnivoltaic Energy Solutions Company Limited
HQ office: FLAT C, 9/F, WINNING HOUSE, NO.72-74, 
WING LOK STREET SHEUNG WAN, HONG KONG
www.omnivoltaic.com
Tel: +86-755-8456 3026
PARTNER VISIT REPORT

Customer Name: SPARK - Kenya. 
Address: Nairobi, Kenya. 
Visit Time: 2nd FEB 2023.

1.	 The purpose of the visit.

1) To check the battery pack status/health of some of the 12AH battery hubs that were faulty.
2) To check the autonomy of some of battery units that were reported by the end users to be draining first.
3) Check whether the packs with faulty cells can still be recovered using a recovery board.

2.	 What we have done.

i.	Did a sample capacity test on one of the packs using the ISDT equipment.
Capacity detected by the equipment=9160 MAH out of the possible 12000 MAH. 
ii.	Trained SPARK’s technician on how to use the recovery board to recover the drained cells and the ISDT equipment to calibrate the whole back and check its potential capacity.

3.	Data
Product	Total Quantity	Quantity with Faulty cells.	Quantity with autonomy issue.	Quantity with other faults.
12AH	43	13	28	2

From the table above the following can be deduced:
•	Most of the complaints are attached to the battery pack,
•	About 65% of the faults are issues to do with autonomy of the batteries that have dropped,
•	About 30% of the faults are battery packs with either one or more cells completely dead and cannot be recovered, and
•	About 5% of them have other issues such as charging and USB ports not functional.

4.	Problems solved.
1) Made sure that SPARK’s technician was able to use effectively the battery recovery tools provided.
2) Made sure that SPARK’s technician was able to prepare a complaint report for the units that had faulty cells.
3) Made sure that the technician was able to use the ISDT equipment to determine the exact current capacities of the units whose autonomies had dropped.

5.	Next step and recommendations.
1)	SPARK’s technician to continue with the shared procedure to solve the problems with the remaining units and in the future.
2)	OVES to provide GA chargers for Camp units to ease the process of charging since use of solar panels to do battery maintenance can be very cumbersome especially when dealing with large stock.
3)	OVES will work on a compensation plan on the packs with faulty cells upon receiving the final complaint report from the technician.
4)	SPARK’s to ensure that going forward, all the returned units have to be charged, discharged and then charged again at least once every three months so as to maintain the battery packs.
5)	SPARK to keep us posted on the battery pack calibration process using ISDT.


	
I OVES technician (Kevin Kibet) confirm that the above mentioned work was carried out for the client.

SIGNATURE	     Date

We, SPARK-Kenya, confirm that the above-mentioned work was carried out by OVES technician. Confirmed by;
NAME: 
SIGNATURE	     Date

"""
while True:
    question = input("Enter your query:")
    output = llm(context + question)
    print (output.strip())
