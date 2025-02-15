//
//  ContentView.swift
//  ReMind
//
//  Created by Jessu Doroy on 2025-02-15.
//

import SwiftUI
import SwiftData

struct ContentView: View {
    @Environment(\.modelContext) private var modelContext
    @Query private var items: [Item]

    var body: some View {
        ZStack{
            Color(red: 0.0, green: 1.0, blue: 1.0)
                .ignoresSafeArea()
            Text("Content View")
             
        }
        
        VStack(alignment: .leading, spacing:15) { //Vertical stack, code location is location on the app
            
            
            
        
            HStack(alignment: .center){
            
                Image("Calm")
                    .resizable() //
                    .aspectRatio(contentMode:.fit) //fits image to the aspect ratio
                    .cornerRadius(20) //rounds the image corners
    
           
            }
            VStack(alignment: .trailing) {
                HStack{ //Horizontality, anything in here is in the same horizontal row
                    Text("Mind")
                        .font(.title)
                        .fontWeight(/*@START_MENU_TOKEN@*/.bold/*@END_MENU_TOKEN@*/)
                    Spacer()
                    HStack{
                        Image(systemName: "star.fill")//SF symbol, search it up for library of symbols
                        Image(systemName: "star.fill")
                        Image(systemName: "star.fill")
                        Image(systemName: "star.fill")
                    }
                    .foregroundColor(.orange)
                    
                        
                }
                Text("Recommended")
            }
            
            Text("Do not forget to take care of yourself :)")
           
        }
            .background(Rectangle().foregroundColor(.blue))
            .padding()
        NavigationSplitView {
            List {
                ForEach(items) { item in
                    NavigationLink {
                        Text("Item at \(item.timestamp, format: Date.FormatStyle(date: .numeric, time: .standard))")
                    } label: {
                        Text(item.timestamp, format: Date.FormatStyle(date: .numeric, time: .standard))
                    }
                }
                .onDelete(perform: deleteItems)
            }
#if os(macOS)
            .navigationSplitViewColumnWidth(min: 180, ideal: 200)
#endif
            .toolbar {
#if os(iOS)
                ToolbarItem(placement: .navigationBarTrailing) {
                    EditButton()
                }
#endif
                ToolbarItem {
                    Button(action: addItem) {
                        Label("Add Item", systemImage: "plus")
                    }
                }
            }
        } detail: {
            Text("Select an item")
        }
    }
       
    private func addItem() {
        withAnimation {
            let newItem = Item(timestamp: Date())
            modelContext.insert(newItem)
        }
    }

    private func deleteItems(offsets: IndexSet) {
        withAnimation {
            for index in offsets {
                modelContext.delete(items[index])
            }
        }
    }
}

#Preview {
    ContentView()
        .modelContainer(for: Item.self, inMemory: true)
}
