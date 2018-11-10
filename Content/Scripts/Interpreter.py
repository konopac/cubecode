import unreal_engine as ue

class Interpreter:

	def interpret(self, code):
		def rollNorth():
			ue.log('north')
			self.uobject.AddToQueue('rollNorth')
			
		def rollSouth():
			ue.log('south')
			self.uobject.AddToQueue('rollSouth')
			
		def rollWest():
			ue.log('west')
			self.uobject.AddToQueue('rollWest')
			
		def rollEast():
			ue.log('east')
			self.uobject.AddToQueue('rollEast')
		
		ue.log('----------')
		exec code in globals(), locals()
		self.uobject.PlayQueue()
		ue.log('----------')