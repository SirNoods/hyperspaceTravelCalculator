import streamlit as st
import app
totaltime = 0
totaljumps = st.text_input("List all your jump points in order, separated by a comma.")
jumplist = totaljumps.split(",")
difficulty = st.number_input("Difficulty")
hyperdriveclass = st.number_input("Hyperdrive Modifier:")
for i in range(len(jumplist)):
    if jumplist[i].startswith(" "):
        jumplist[i] = jumplist[i][1:]

#st.write(jumplist)
for i in range(len(jumplist)-1):
    start = app.galaxy_map.get_territory(jumplist[i])
    end = app.galaxy_map.get_territory(jumplist[i+1])
    st.write("You are jumping from "+ jumplist[i] + " to " + jumplist[i+1] + ", taking you " + str(((app.region_to_region_travel_times[start][end]/2)/hyperdriveclass)) + " hours.")
    totaltime += ((difficulty*app.region_to_region_travel_times[start][end])/hyperdriveclass)/2

st.write("Your jump takes "+ str(totaltime)+ " hours.")