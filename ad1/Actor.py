#!/usr/bin/env python
# coding: UTF-8
#
# @package Actor

##
#
# Actor class, which is the base class for Disease objects.
#
# Resolução da AD1 2020.2 - Prog. de Interfaces Gráficas - TSC/UFF
# @author ARIADNE GONÇALVES PINHEIRO
# Matrícula: 19113050151
# Pólo: Duque de Caxias
# @date 26/08/2020
#

class Actor:
    # Holds the value of the next "free" id.
    __ID = 0

    ##
    # Construct a new Actor object.
    # - Sets the initial values of its member variables.
    # - Sets the unique ID for the object and initializes the reference to the World
    #   object to which this Actor object belongs to null.
    # - The ID of the first Actor object is 0.
    # - The ID gets incremented by one each time a new Actor object is created.
    # - Sets the iteration counter to zero and initialize the location of the
    #   object to cell (0,0).
    #
    def __init__(self):
        # X coordinate of this actor.
        self.__locX = 0
        # Y coordinate of this actor.
        self.__locY = 0
        # World this actor belongs to.
        self.__world = None
        # Unique identifier for this actor.
        self.__actorID = Actor.__ID
        Actor.__ID += 1
        # Iteration counter.
        self.__itCounter = 0

    ##
    # Used for testing
    # @return ActorID
    #
    def getID(self):
        return self.__actorID

    ##
    # Used for testing
    # @return number of iterations
    #
    def Iteration(self):
        return self.__itCounter

    ##
    # Prints on screen in the format "Iteration <ID>: Actor <Actor ID>".
    #
    # The @f$<ID>@f$ is replaced by the current iteration number. @f$<Actor ID>@f$ is
    # replaced by the unique ID of the Actor object that performs the act(self)
    # method.
    #
    # For instance, the actor with ID 1 shows the following result on
    # the output screen after its act(self) method has been called twice.
    # <PRE>
    # Iteration 0: Actor 1
    # Iteration 1: Actor 1
    # </PRE>
    #
    def act(self):
        print("Iteration {}: Actor {}".format(self.__itCounter, self.__actorID))
        self.__itCounter += 1

    ##
    # Sets the cell coordinates of this object.
    #
    # @param x the column.
    # @param y the row.
    #
    # @throws ValueError when x < 0 or x >= world width,
    # @throws ValueError when y < 0 or y >= world height,
    # @throws RuntimeError when the world is null.
    #
    def setLocation(self, x, y):
        if self.__world is None:
            raise RuntimeError
        if (0 <= x < self.__world.getWidth()) and (0 <= y < self.__world.getHeight()):
            self.__locX = x
            self.__locY = y
        else:
            raise ValueError

    ##
    # Sets the world this actor is into.
    #
    # @param world Reference to the World object this Actor object is added.
    # @throws RuntimeError when world is null.
    #
    def addedToWorld(self, world):
        if world is None:
            raise RuntimeError

        self.__world = world

    ##
    # Gets the world this object in into.
    #
    # @return the world this object belongs to
    #
    def getWorld(self):
        return self.__world

    ##
    # Gets the X coordinate of the cell this actor object is into.
    #
    # @return the x coordinate of this Actor object.
    #
    def getX(self):
        return self.__locX

    ##
    # Gets the Y coordinate of the cell this actor object is into.
    #
    # @return the y coordinate of this Actor object.
    #
    def getY(self):
        return self.__locY

    ##
    #  Return a string with this actor ID and position.
    #
    def __str__(self):
        try:
            st = "ID = %d "u'\u2192 '.encode('utf-8') % self.getID()
            st += 'position = (%d, %d)\n' % (self.getX(), self.getY())
        except TypeError:
            st = "ID = %d "u'\u2192 ' % self.getID()
            st += 'position = (%d, %d)\n' % (self.getX(), self.getY())
        return st
