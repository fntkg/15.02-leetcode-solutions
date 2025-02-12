class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        # Initialize the current altitude to 0
        current_altitude = 0

        # Initialize the highest altitude to the current altitude
        highest_altitude = current_altitude

        # Iterate through each net gain in the gain list
        for net_gain in gain:
            # Update the current altitude by adding the net gain
            current_altitude += net_gain
            # Update the highest altitude if the current altitude is greater
            highest_altitude = max(highest_altitude, current_altitude)

        # Return the highest altitude reached
        return highest_altitude