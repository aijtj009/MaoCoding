"""
 AT
 BY
 IN
 OF
 ON
+TO
------
BET
"""

def Find():
	fileout = open("foo.txt", "w")
	for a in range(1,10):
		for t in range(1,10):
			for b in range(1,3):
				for y in range(10):
					for i in range(1,10):
						for n in range(10):
							for o in range(1,10):
								for f in range(10):
									for e in range(10):
										if (a!=t) and (a!=b) and (a!=y) and (a!=i) and (a!=n) and (a!=o) and (a!=f) and (a!=e):
											if (t!=b) and (t!=y) and (t!=i) and (t!=n) and (t!=o) and (t!=f) and (t!=e):
												if (b!=y) and (b!=i) and (b!=n) and (b!=o) and (b!=f) and (b!=e):
													if (y!=i) and (y!=n) and (y!=o) and (y!=f) and (y!=e) :
														if (i!=n) and (i!=o) and (i!=f) and (i!=e):
															if (n!=o) and (n!=f) and (n!=e):
																if (o!=f) and (o!=e):
																	if (f!=e):
																		if (a*10+t+b*10+y+i*10+n+o*10+f+o*10+n+t*10+o==b*100+e*10+t):
																			fileout.write("Solved: A={},T={},B={},Y={},I={},N={},O={},F={},E={}\n".format(a,t,b,y,i,n,o,f,e))
	fileout.close()

if __name__=="__main__":
    Find()
