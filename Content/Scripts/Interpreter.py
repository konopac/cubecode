import unreal_engine as ue

class Interpreter:

	def interpret(self, code):
		def rollNorth():
			ue.log('rollNorth')
			self.uobject.AddToQueue('rollNorth')
			
		def rollSouth():
			ue.log('rollSouth')
			self.uobject.AddToQueue('rollSouth')
			
		def rollWest():
			ue.log('rollWest')
			self.uobject.AddToQueue('rollWest')
			
		def rollEast():
			ue.log('rollEast')
			self.uobject.AddToQueue('rollEast')
		
		def checkNorth():
			ue.log('checkNorth')
			self.uobject.AddToQueue('checkNorth')
			return True
		
		def checkSouth():
			ue.log('checkSouth')
			self.uobject.AddToQueue('checkSouth')
			return True
			
		def checkWest():
			ue.log('checkWest')
			self.uobject.AddToQueue('checkWest')
			return True
			
		def checkEast():
			ue.log('checkEast')
			self.uobject.AddToQueue('checkEast')
			return True

		ue.log('----------')
		exec code in globals(), locals()
		self.uobject.PlayQueue()
		ue.log('----------')