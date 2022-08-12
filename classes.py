class Television:
    '''
    A class for representing details for a TV object
    '''
    MIN_CHANNEL: int = 0     # Minimum TV channel
    MAX_CHANNEL: int = 3     # Maximum TV channel

    MIN_VOLUME: int = 0      # Minimum TV volume
    MAX_VOLUME: int = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor to create a new TV
        """
        self.__channel = 0
        self.__volume = 0
        self.__status = 'off'

    def power(self) -> None:
        """
        This method will turn the TV on or off
        """
        if self.__status == 'off':
            self.__status = 'on'
        else:
            self.__status = 'off'

    def channel_up(self) -> None:
        """
        This method will increase the channel one
        """
        if self.__status == 'on':
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        This method will decrease the channel one
        """
        if self.__status == 'on':
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increases the volume one stopping at the max volume
        """
        if self.__status == 'on':
            self.__volume += 1
            if self.__volume > Television.MAX_VOLUME:
                self.__volume -= 1

    def volume_down(self) -> None:
        """
        Decreases volume by one stopping at the minimum value
        """
        if self.__status == 'on':
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        This method should be used to return the TV status
        """
        if self.__status == 'on':
            __onoff: str = 'True'
        else:
            __onoff: str = 'False'

        # TV status: Is on = True, Channel = 1, Volume = 1
        return f'TV status: Is on = {__onoff}, Channel = {self.__channel}, Volume = {self.__volume}'
