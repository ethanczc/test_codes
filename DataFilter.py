# Demo class, imported by getMean.py
import statistics
class DataFilter:
	@staticmethod
	def GetMean(sample):
		stdDev = round(statistics.stdev(sample),3)
		mean = round(statistics.mean(sample),3)
		lowerLimit = mean - stdDev
		upperLimit = mean + stdDev
		trueSample = []
		for i in sample:
			if i > lowerLimit and i < upperLimit:
				trueSample.append(i)
		trueMean = round(statistics.mean(trueSample),3)
		return trueMean