package de.starwit;

import java.util.HexFormat;

import com.google.protobuf.ByteString;
import com.google.protobuf.InvalidProtocolBufferException;

import de.starwit.visionapi.Messages.BoundingBox;
import de.starwit.visionapi.Messages.Detection;
import de.starwit.visionapi.Messages.SaeMessage;
import de.starwit.visionapi.Messages.Shape;
import de.starwit.visionapi.Messages.VideoFrame;

/**
 * Sample code, that shall demonstrate, how to use generated Protobuf classes.
 */
public class App {
    public static void main(String[] args) {
        System.out.println("Testing generated classes");

        // VideoSource classes

        // fake an image
        byte[] bytes = HexFormat.of().parseHex("e04fd020ea3a6910a2d808002b30309d");               
        
        Shape shape1 = Shape.newBuilder()
            .setHeight(1080)
            .setWidth(1920)
            .setChannels(3)
            .build();

        VideoFrame vf = VideoFrame.newBuilder()
            .setShape(shape1)
            .setFrameData(ByteString.copyFrom(bytes))
            .build();

        byte[] serializedObjects = vf.toByteArray();
        System.out.println("Serialized objects " + serializedObjects);

        try {
            VideoFrame parsedVF = VideoFrame.parseFrom(serializedObjects);
            System.out.println(parsedVF.getShape().getHeight());
        } catch(InvalidProtocolBufferException e) {
            System.out.println("can't parse protobuf from bytes");
        }

        // Detector
        BoundingBox bb =  BoundingBox.newBuilder()
            .setMinX(1)
            .setMinY(1)
            .setMaxX(10)
            .setMaxY(10)
            .build();
        Detection d = Detection.newBuilder()
            .setBoundingBox(bb)
            .setConfidence((float)0.5)
            .setClassId(0)
            .build();

        SaeMessage detMessage = SaeMessage.newBuilder()
            .addDetections(d)
            .build();

        serializedObjects = detMessage.toByteArray();
        
        try {
            SaeMessage parsedDetMsg = SaeMessage.parseFrom(serializedObjects);
            System.out.println(parsedDetMsg.getDetections(0).getConfidence());
        } catch (InvalidProtocolBufferException e) {
            System.out.println("can't parse protobuf from bytes");
        }


        // Tracker
        //
        byte[] sampleTrackingID = {0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09};
        Detection det = Detection.newBuilder()
            .setBoundingBox(bb)
            .setConfidence((float)0.5)
            .setClassId(0)
            .setObjectId(ByteString.copyFrom(sampleTrackingID))
            .build();

        SaeMessage trackMessage = SaeMessage.newBuilder()
            .addDetections(det)
            .build();

        serializedObjects = trackMessage.toByteArray();

        try {
            SaeMessage trackMsgOut = SaeMessage.parseFrom(serializedObjects);
            System.out.println(trackMsgOut.getDetections(0).getClassId());
        } catch (InvalidProtocolBufferException e) {
            System.out.println("can't parse protobuf from bytes");
        }        

    }
}
